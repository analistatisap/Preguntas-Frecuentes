from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST # type: ignore
import json
import os
import logging

# Asegúrate de que 'ldap3' esté en tu archivo requirements.txt
from ldap3 import Server, Connection, ALL

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
            return JsonResponse({'error': 'Usuario y contraseña son requeridos'}, status=400)

        if not LDAP_BIND_PASSWORD:
            print("Error Crítico: La variable de entorno LDAP_BIND_PASSWORD no está configurada en el servidor.")
            return JsonResponse({'error': 'Error de configuración del servidor.'}, status=500)

        search_filter = f'(&(sAMAccountName={username})(&(objectClass=user)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2))))'

        # Configuración TLS para LDAPS
        tls_configuration = None
        if LDAP_TLS_CACERT:
            try:
                import ssl
                from ldap3 import Tls
                # Asegúrate de que el archivo de certificado exista y sea accesible
                if not os.path.exists(LDAP_TLS_CACERT):
                    print(f"Advertencia: El archivo de certificado CA '{LDAP_TLS_CACERT}' no se encontró en la ruta especificada.")
                    # Para producción, es crucial que esto funcione. Considera fallar aquí o usar un certificado válido.
                    tls_configuration = Tls(validate=ssl.CERT_NONE) # No recomendado para producción: deshabilita la validación
                else:
                    tls_configuration = Tls(validate=ssl.CERT_REQUIRED, ca_certs_file=LDAP_TLS_CACERT)
            except ImportError:
                print("Advertencia: El módulo 'ssl' no está disponible o 'ldap3.Tls' no se pudo importar. No se aplicará la validación de certificado TLS.")
                tls_configuration = Tls(validate=ssl.CERT_NONE) # Fallback, no seguro

        # Determinar si usar SSL basado en el puerto
        use_ssl = (LDAP_PORT == 636)

        server = Server(LDAP_SERVER, port=LDAP_PORT, use_ssl=use_ssl, tls=tls_configuration, get_info=ALL)
        
        # 1. Conexión con la cuenta de servicio para buscar al usuario
        try:
            conn = Connection(server, user=LDAP_BIND_USER_DN, password=LDAP_BIND_PASSWORD, auto_bind=True)
            if not conn.bound: # Verificar si la conexión fue exitosa
                print(f"Error: Falló la conexión/bind con el usuario de servicio LDAP: {conn.result}")
                return JsonResponse({'error': 'Error interno del servidor al conectar con el Directorio Activo.'}, status=500)
        except Exception as e:
            print(f"Error al intentar conectar/bind con el usuario de servicio LDAP: {e}")
            return JsonResponse({'error': 'Error interno del servidor al conectar con el Directorio Activo.'}, status=500)

        # 2. Buscar al usuario para obtener su DN (Distinguished Name) completo
        conn.search(search_base=LDAP_BASE_DN,
                    search_filter=search_filter,
                    attributes=['distinguishedName', 'cn', 'mail'])

        if not conn.entries:
            conn.unbind()
            print(f"Error: Usuario '{username}' no encontrado o deshabilitado en LDAP.")
            return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401)

        user_entry = conn.entries[0]
        user_dn = user_entry.distinguishedName.value
        conn.unbind()
        
        # 3. Intentar una nueva conexión con las credenciales del usuario para validar la contraseña
        try:
            user_conn = Connection(server, user=user_dn, password=password, auto_bind=True)
            if not user_conn.bound: # Verificar si la conexión fue exitosa
                print(f"Error: Falló la autenticación del usuario '{username}' con DN '{user_dn}': {user_conn.result}")
                return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401)
        except Exception as e:
            print(f"Error al intentar autenticar al usuario '{username}' con DN '{user_dn}': {e}")
            return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401) # O 500 si es un error de conexión

        user_info = {
            'username': username,
            'fullName': user_entry.cn.value if user_entry.cn else '',
            'email': user_entry.mail.value if user_entry.mail else ''
        }
        user_conn.unbind()
        return JsonResponse({'status': 'success', 'user': user_info}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Cuerpo de la petición inválido (no es JSON).'}, status=400)
    except Exception as e: # Captura cualquier otra excepción no manejada y la loguea
        logging.error(f"Error inesperado en login_ldap_view: {e}", exc_info=True) # exc_info=True para imprimir el traceback
        return JsonResponse({'error': 'Error interno del servidor durante la autenticación.'}, status=500)

# --- Vistas de ejemplo para otros endpoints ---
@csrf_exempt
def enviar_correo_view(request):
    return JsonResponse({'message': 'Endpoint de enviar correo (por implementar)'})

def obtener_manuales_view(request):
    return JsonResponse({'message': 'Endpoint de manuales (por implementar)'})

def obtener_tips_view(request):
    return JsonResponse({'message': 'Endpoint de tips (por implementar)'})
