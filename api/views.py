from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import os
import logging

# Asegúrate de que 'ldap3' esté en tu archivo requirements.txt
from ldap3 import Server, Connection, ALL, Tls
from ldap3.core.exceptions import LDAPBindError, LDAPException

# --- Configuración de LDAP ---
# ¡IMPORTANTE! Estos valores deben ser configurados como variables de entorno en tu entorno de Podman/Docker.
LDAP_SERVER = os.environ.get('LDAP_SERVER', '10.10.10.4')
LDAP_PORT = int(os.environ.get('LDAP_PORT', 389)) # Usar 636 para LDAPS (recomendado)
LDAP_BASE_DN = os.environ.get('LDAP_BASE_DN', 'OU=Usuarios,OU=01 - GRUPODECOR,DC=grupodecor,DC=local')
LDAP_BIND_USER_DN = os.environ.get('LDAP_BIND_USER_DN', 'CN=Andres Felipe Viveros Alban,OU=Decor SAP,OU=TI,OU=Oficina Principal,OU=Usuarios,OU=01 - GRUPODECOR,DC=grupodecor,DC=local')
LDAP_BIND_PASSWORD = os.environ.get('LDAP_BIND_PASSWORD')
# Opcional: Ruta al certificado CA para LDAPS. Necesario si el servidor AD usa un certificado no confiable por defecto.
LDAP_TLS_CACERT = os.environ.get('LDAP_TLS_CACERT', None)

@csrf_exempt
@require_POST
def login_ldap_view(request):
    conn = None
    user_conn = None
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            logging.warning("Intento de login con usuario o contraseña vacíos.")
            return JsonResponse({'error': 'Usuario y contraseña son requeridos'}, status=400)

        if not LDAP_BIND_PASSWORD:
            logging.critical("CRITICAL: La variable de entorno LDAP_BIND_PASSWORD no está configurada.")
            return JsonResponse({'error': 'Error de configuración del servidor.'}, status=500)

        search_filter = f'(&(sAMAccountName={username})(&(objectClass=user)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2))))'

        # --- Configuración de Servidor y TLS para LDAPS ---
        tls_config = None
        use_ssl = (LDAP_PORT == 636)
        if use_ssl:
            try:
                import ssl
                if LDAP_TLS_CACERT and os.path.exists(LDAP_TLS_CACERT):
                    logging.info(f"Usando certificado CA desde: {LDAP_TLS_CACERT}")
                    tls_config = Tls(validate=ssl.CERT_REQUIRED, ca_certs_file=LDAP_TLS_CACERT)
                else:
                    logging.warning("LDAPS configurado sin un archivo CA válido. La validación del certificado está deshabilitada (NO SEGURO).")
                    tls_config = Tls(validate=ssl.CERT_NONE)
            except ImportError:
                logging.error("El módulo 'ssl' no está disponible. No se puede configurar TLS para LDAPS.")
                return JsonResponse({'error': 'Error de configuración del servidor para LDAPS.'}, status=500)

        server = Server(LDAP_SERVER, port=LDAP_PORT, use_ssl=use_ssl, tls=tls_config, get_info=ALL)
        
        # 1. Conexión con la cuenta de servicio para buscar al usuario
        logging.info(f"Intentando bind con usuario de servicio: {LDAP_BIND_USER_DN}")
        conn = Connection(server, user=LDAP_BIND_USER_DN, password=LDAP_BIND_PASSWORD, auto_bind=True)
        if not conn.bound:
            logging.error(f"Falló el bind con el usuario de servicio. Resultado: {conn.result}")
            return JsonResponse({'error': 'Error interno del servidor al conectar con el Directorio Activo.'}, status=500)
        
        # 2. Buscar al usuario para obtener su DN (Distinguished Name) completo
        logging.info(f"Buscando usuario '{username}' con filtro: {search_filter}")
        conn.search(search_base=LDAP_BASE_DN,
                    search_filter=search_filter,
                    attributes=['distinguishedName', 'cn', 'mail'])

        if not conn.entries:
            logging.warning(f"Usuario '{username}' no encontrado o cuenta deshabilitada en LDAP.")
            return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401)

        user_entry = conn.entries[0]
        user_dn = user_entry.distinguishedName.value
        logging.info(f"Usuario '{username}' encontrado con DN: {user_dn}")
        
        # 3. Intentar una nueva conexión con las credenciales del usuario para validar la contraseña
        logging.info(f"Intentando autenticar al usuario con DN: {user_dn}")
        user_conn = Connection(server, user=user_dn, password=password, auto_bind=True)
        if not user_conn.bound:
            logging.warning(f"Autenticación fallida para el usuario '{username}'. Resultado: {user_conn.result}")
            return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401)
        
        logging.info(f"Autenticación exitosa para el usuario '{username}'.")
        user_info = {
            'username': username,
            'fullName': user_entry.cn.value if user_entry.cn else '',
            'email': user_entry.mail.value if user_entry.mail else ''
        }
        
        return JsonResponse({'status': 'success', 'user': user_info}, status=200)

    except json.JSONDecodeError:
        logging.warning("Cuerpo de la petición inválido (no es JSON).")
        return JsonResponse({'error': 'Cuerpo de la petición inválido (no es JSON).'}, status=400)
    except LDAPBindError as e:
        # Esto puede ocurrir si las credenciales del usuario de servicio son incorrectas
        logging.error(f"Error de Bind LDAP: {e}", exc_info=True)
        return JsonResponse({'error': 'Error de credenciales del servicio de autenticación.'}, status=500)
    except LDAPException as e:
        # Captura otras excepciones de ldap3
        logging.error(f"Error de LDAP: {e}", exc_info=True)
        return JsonResponse({'error': 'Error de comunicación con el servicio de autenticación.'}, status=500)
    except Exception as e:
        logging.error(f"Error inesperado en login_ldap_view: {e}", exc_info=True)
        return JsonResponse({'error': 'Error interno del servidor durante la autenticación.'}, status=500)
    finally:
        # Asegurarse de que ambas conexiones se cierren
        if conn and conn.bound:
            conn.unbind()
        if user_conn and user_conn.bound:
            user_conn.unbind()

# --- Vistas de ejemplo para otros endpoints ---
@csrf_exempt
def enviar_correo_view(request):
    return JsonResponse({'message': 'Endpoint de enviar correo (por implementar)'})

def obtener_manuales_view(request):
    return JsonResponse({'message': 'Endpoint de manuales (por implementar)'})

def obtener_tips_view(request):
    return JsonResponse({'message': 'Endpoint de tips (por implementar)'})