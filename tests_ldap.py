import os
from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPBindError, LDAPSocketOpenError


# URL del servidor Active Directory
# Usa ldap:// para puerto 389 o ldaps:// para puerto 636 (seguro)
LDAP_SERVER_URI_TEST = 'ldap://10.10.10.4:389'

# Credenciales del usuario de servicio para el bind (lectura del AD)
# Este usuario necesita permisos de lectura en tu AD.
LDAP_BIND_DN_TEST = 'CN=jagrajales,OU=Usuarios,DC=grupodecor,DC=local'
LDAP_BIND_PASSWORD_TEST = 'Decor2025##' # Contraseña REAL de tu usuario de servicio

# Base DN (Distinguished Name) donde buscar usuarios
# Esta es la ruta correcta identificada para tus usuarios.
LDAP_USER_SEARCH_BASE_DN_TEST = 'OU=Usuarios,OU=01 - GRUPODECOR,DC=grupodecor,DC=local'

# --- FIN DE LA CONFIGURACIÓN LDAP ---

print(f"--- Iniciando prueba de conexión LDAP ---")
print(f"Servidor LDAP: {LDAP_SERVER_URI_TEST}")
print(f"Usuario de bind: {LDAP_BIND_DN_TEST}")
print(f"Base DN para búsqueda de usuarios: {LDAP_USER_SEARCH_BASE_DN_TEST}")
print("-" * 40)

try:
    # 1. Crear un objeto Server
    server = Server(LDAP_SERVER_URI_TEST, get_info=ALL)
    
    # 2. Crear una conexión y intentar autenticar al usuario de servicio (bind)
    # auto_bind=True intenta autenticar automáticamente al usuario de servicio
    # con las credenciales proporcionadas al crear la conexión.
    print("Intentando bind (autenticación) con el usuario de servicio...")
    conn = Connection(
        server,
        user=LDAP_BIND_DN_TEST,
        password=LDAP_BIND_PASSWORD_TEST,
        auto_bind=True
    )

    # 3. Verificar si el bind del usuario de servicio fue exitoso
    if conn.bound:
        print("¡Bind (autenticación) del usuario de servicio exitoso!")

        test_user_samaccountname = 'ltrejos'
        search_filter = f'(sAMAccountName={test_user_samaccountname})'
        
        print(f"\nIntentando buscar al usuario '{test_user_samaccountname}'...")
        print(f"Filtro de búsqueda: '{search_filter}' en Base DN: '{LDAP_USER_SEARCH_BASE_DN_TEST}'")
        
        conn.search(LDAP_USER_SEARCH_BASE_DN_TEST, search_filter, attributes=['cn', 'mail', 'sAMAccountName'])

        if conn.entries:
            print(f"\n¡Usuario '{test_user_samaccountname}' encontrado en Active Directory!")
            for entry in conn.entries:
                print(f"  DN del usuario: {entry.entry_dn}")
                if 'cn' in entry:
                    print(f"  Common Name (cn): {entry.cn.value}")
                if 'mail' in entry:
                    print(f"  Email: {entry.mail.value}")
                if 'sAMAccountName' in entry:
                    print(f"  sAMAccountName: {entry.sAMAccountName.value}")
            
            # Intentar autenticar el usuario final con su propia contraseña
            print(f"\n--- Intentando autenticar al usuario final '{test_user_samaccountname}' ---")
            TEST_USER_PASSWORD = 'Decor2024*'

            try:
                user_conn = Connection(server, user=test_user_samaccountname, password=TEST_USER_PASSWORD, auto_bind=True)
                if user_conn.bound:
                    print(f"¡Autenticación exitosa para el usuario '{test_user_samaccountname}' con sus credenciales!")
                else:
                    print(f"Fallo en la autenticación para el usuario '{test_user_samaccountname}'. Resultado: {user_conn.result}")
                user_conn.unbind()
            except LDAPBindError as e:
                print(f"Error de autenticación para el usuario '{test_user_samaccountname}': {e}")
            except Exception as e:
                print(f"Error inesperado al intentar autenticar al usuario final: {e}")

        else:
            print(f"ERROR: Usuario '{test_user_samaccountname}' NO ENCONTRADO en la Base DN especificada.")
            print(f"Detalles del resultado de búsqueda: {conn.result}")
            print("Verifica si la 'LDAP_USER_SEARCH_BASE_DN_TEST' es correcta o si el usuario está en esa OU.")
            print("También confirma que el 'sAMAccountName' es exactamente correcto.")

    else:
        print(f"ERROR: Fallo en el bind (autenticación) con el usuario de servicio '{LDAP_BIND_DN_TEST}'.")
        print(f"Resultado: {conn.result}")
        print("Verifica si el LDAP_BIND_DN_TEST y LDAP_BIND_PASSWORD_TEST son correctos y si el usuario de servicio tiene permisos.")

except LDAPBindError as e:
    print(f"ERROR CRÍTICO: Error de autenticación inicial con el usuario de servicio: {e}")
    print("Esto puede indicar credenciales incorrectas para el usuario de servicio o problemas de permiso.")
except LDAPSocketOpenError as e:
    print(f"ERROR CRÍTICO: No se pudo conectar al servidor LDAP: {e}")
    print("Verificar la IP y el puerto (ej. 10.10.10.4:389). Asegúrate de que no haya un firewall bloqueando la conexión.")
    print("También, confirma que el servidor LDAP está en línea y accesible desde donde ejecutas este script.")
except Exception as e:
    print(f"ERROR INESPERADO durante la prueba: {e}")

finally:
    if 'conn' in locals() and conn.bound:
        print("\nDesconectando del servidor LDAP (conexión de servicio).")
        conn.unbind()
    print("\n--- Prueba de conexión LDAP finalizada ---")