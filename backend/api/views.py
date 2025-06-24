from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST # type: ignore
import json
import os
import logging

# Asegúrate de que 'ldap3' esté en tu archivo requirements.txt
from ldap3 import Server, Connection, ALL, Tls # Import Tls directamente

# --- Configuración de LDAP ---
# ¡IMPORTANTE! Estos valores deben ser configurados como variables de entorno en tu entorno de Podman/Docker.
LDAP_SERVER = os.environ.get('LDAP_SERVER', '10.10.10.4')
LDAP_PORT = int(os.environ.get('LDAP_PORT', 389))
LDAP_BASE_DN = os.environ.get('LDAP_BASE_DN', 'OU=Usuarios,OU=01 - GRUPODECOR,DC=grupodecor,DC=local')
LDAP_BIND_USER_DN = os.environ.get('LDAP_BIND_USER_DN', 'CN=Andres Felipe Viveros Alban,OU=Decor SAP,OU=TI,OU=Oficina Principal,OU=Usuarios,OU=01 - GRUPODECOR,DC=grupodecor,DC=local')
LDAP_BIND_PASSWORD = os.environ.get('LDAP_BIND_PASSWORD')

# Opcional: Ruta al certificado CA para LDAPS. Solo necesario si usas LDAPS (puerto 636)
# y tu servidor AD usa un certificado autofirmado o de una CA interna no confiable por defecto.
LDAP_TLS_CACERT = os.environ.get('LDAP_TLS_CACERT', None)

@csrf_exempt
@require_POST
def login_ldap_view(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            logging.warning("Intento de login con usuario o contraseña vacíos.")
            return JsonResponse({'error': 'Usuario y contraseña son requeridos'}, status=400)

        if not LDAP_BIND_PASSWORD:
            logging.critical("Error Crítico: La variable de entorno LDAP_BIND_PASSWORD no está configurada en el servidor.")
            return JsonResponse({'error': 'Error de configuración del servidor.'}, status=500)

        search_filter = f'(&(sAMAccountName={username})(&(objectClass=user)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2))))'

        # Configuración TLS para LDAPS
        tls_configuration = None
        if LDAP_TLS_CACERT:
            try:
                import ssl
                # from ldap3 import Tls # Ya importado
                # Asegúrate de que el archivo de certificado exista y sea accesible
                if not os.path.exists(LDAP_TLS_CACERT):
                    logging.warning(f"Advertencia: El archivo de certificado CA '{LDAP_TLS_CACERT}' no se encontró en la ruta especificada. Se intentará la conexión sin validación de certificado.")
                    # Para producción, es crucial que esto funcione. Considera fallar aquí o usar un certificado válido.
                    tls_configuration = Tls(validate=ssl.CERT_NONE) # No recomendado para producción: deshabilita la validación
                else:
                    tls_configuration = Tls(validate=ssl.CERT_REQUIRED, ca_certs_file=LDAP_TLS_CACERT)
            except ImportError:
                logging.error("Advertencia: El módulo 'ssl' no está disponible o 'ldap3.Tls' no se pudo importar. No se aplicará la validación de certificado TLS.", exc_info=True)
                tls_configuration = Tls(validate=ssl.CERT_NONE) # Fallback, no seguro
            except Exception as e:
                logging.error(f"Error al configurar TLS con certificado CA: {e}", exc_info=True)
                tls_configuration = Tls(validate=ssl.CERT_NONE) # Fallback, no seguro



        # Determinar si usar SSL basado en el puerto
        use_ssl = (LDAP_PORT == 636)

        server = Server(LDAP_SERVER, port=LDAP_PORT, use_ssl=use_ssl, tls=tls_configuration, get_info=ALL)
        
        # 1. Conexión con la cuenta de servicio para buscar al usuario
        conn = None # Inicializar conn a None
        try:
            conn = Connection(server, user=LDAP_BIND_USER_DN, password=LDAP_BIND_PASSWORD, auto_bind=True)
            if not conn.bound: # Verificar si la conexión fue exitosa
                logging.error(f"Falló la conexión/bind con el usuario de servicio LDAP. Resultado: {conn.result}")
                return JsonResponse({'error': 'Error interno del servidor al conectar con el Directorio Activo.'}, status=500)
        except Exception as e:
            logging.error(f"Excepción al intentar conectar/bind con el usuario de servicio LDAP: {e}", exc_info=True)
            return JsonResponse({'error': 'Error interno del servidor al conectar con el Directorio Activo.'}, status=500)
        finally:
            if conn and conn.bound:
                conn.unbind() # Asegurar que la conexión se cierre

        # 2. Buscar al usuario para obtener su DN (Distinguished Name) completo
        # Re-establecer la conexión para la búsqueda
        try:
            conn = Connection(server, user=LDAP_BIND_USER_DN, password=LDAP_BIND_PASSWORD, auto_bind=True)
            if not conn.bound:
                logging.error(f"Falló la reconexión/bind para la búsqueda de usuario. Resultado: {conn.result}")
                return JsonResponse({'error': 'Error interno del servidor al conectar con el Directorio Activo.'}, status=500)

            conn.search(search_base=LDAP_BASE_DN,
                        search_filter=search_filter,
                        attributes=['distinguishedName', 'cn', 'mail'])

            if not conn.entries:
                logging.warning(f"Usuario '{username}' no encontrado o deshabilitado en LDAP. Filtro: {search_filter}")
                return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401)

            user_entry = conn.entries[0]
            user_dn = user_entry.distinguishedName.value
        except Exception as e:
            logging.error(f"Excepción durante la búsqueda de usuario LDAP para '{username}': {e}", exc_info=True)
            return JsonResponse({'error': 'Error interno del servidor al buscar usuario en Directorio Activo.'}, status=500)
        finally:
            if conn and conn.bound:
                conn.unbind()
        
        # 3. Intentar una nueva conexión con las credenciales del usuario para validar la contraseña
        user_conn = None # Inicializar user_conn a None
        try:
            user_conn = Connection(server, user=user_dn, password=password, auto_bind=True)
            if not user_conn.bound: # Verificar si la conexión fue exitosa
                logging.warning(f"Falló la autenticación del usuario '{username}' con DN '{user_dn}'. Resultado: {user_conn.result}")
                return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401)
        except Exception as e:
            logging.warning(f"Excepción al intentar autenticar al usuario '{username}' con DN '{user_dn}': {e}", exc_info=True)
            return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401) # O 500 si es un error de conexión
        finally:
            if user_conn and user_conn.bound:
                user_conn.unbind()

        user_info = {
            'username': username,
            'fullName': user_entry.cn.value if user_entry.cn else '',
            'email': user_entry.mail.value if user_entry.mail else ''
        }
        return JsonResponse({'status': 'success', 'user': user_info}, status=200)

    except json.JSONDecodeError:
        logging.warning("Cuerpo de la petición inválido (no es JSON).")
        return JsonResponse({'error': 'Cuerpo de la petición inválido (no es JSON).'}, status=400)
    except Exception as e:
        logging.error(f"Error inesperado en login_ldap_view: {e}", exc_info=True)
        return JsonResponse({'error': 'Error interno del servidor durante la autenticación.'}, status=500)

# --- Vistas de ejemplo para otros endpoints ---
@csrf_exempt
def enviar_correo_view(request):
    return JsonResponse({'message': 'Endpoint de enviar correo (por implementar)'})

def obtener_manuales_view(request):
    return JsonResponse({'message': 'Endpoint de manuales (por implementar)'})

def obtener_tips_view(request):
    return JsonResponse({'message': 'Endpoint de tips (por implementar)'})
