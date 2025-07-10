# Guía de Despliegue en Coolify - Pregúntame

## Configuración para Coolify

### 1. Preparación del Repositorio

Tu aplicación ya está configurada para Coolify con los siguientes archivos:

- `docker-compose.prod.yml` - Configuración de producción
- `nginx/nginx.conf` - Configuración del proxy reverso
- `env.example` - Variables de entorno de ejemplo

### 2. Configuración en Coolify

#### Paso 1: Crear Nueva Aplicación
1. Accede a tu panel de Coolify
2. Crea una nueva aplicación
3. Nombre: `preguntame`
4. Tipo: `Docker Compose`

#### Paso 2: Configurar Repositorio
- **URL del repositorio**: Tu repositorio Git
- **Rama**: `main` o `master`
- **Docker Compose File**: `docker-compose.prod.yml`

#### Paso 3: Configurar Variables de Entorno
Agrega las siguientes variables en Coolify:

```bash
# Django
SECRET_KEY=tu_clave_secreta_muy_segura_aqui
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=nexusti.grupodecor.com,52.177.69.18

# Base de datos
POSTGRES_DB=preguntas_frecuentes
POSTGRES_USER=preguntas
POSTGRES_PASSWORD=una_contraseña_segura_aqui

# Email
EMAIL_HOST=smtp.office365.com
EMAIL_PORT=587
EMAIL_HOST_USER=notificacionesaplicativoweb@grupodecor.com
EMAIL_HOST_PASSWORD=1Ngr3s0W3b2024*
DEFAULT_FROM_EMAIL=notificacionesaplicativoweb@grupodecor.com

# LDAP (configurar según tu servidor)
LDAP_SERVER=tu_servidor_ldap
LDAP_PORT=389
LDAP_BIND_USER_DN=tu_usuario_ldap
LDAP_BIND_PASSWORD=tu_password_ldap
LDAP_BASE_DN=tu_base_dn_ldap
```

#### Paso 4: Configurar Dominio
- **Dominio**: `nexusti.grupodecor.com`
- **IP Pública**: `52.177.69.18`
- **SSL**: Habilitar (Coolify manejará los certificados)

#### Paso 5: Configurar Puertos
- **Puerto principal**: `80`
- **Puerto SSL**: `443`

### 3. Configuración de DNS

Asegúrate de que el subdominio `nexusti.grupodecor.com` apunte a la IP `52.177.69.18`:

```
nexusti.grupodecor.com.  IN  A  52.177.69.18
```

### 4. Estructura de Servicios

La aplicación se desplegará con los siguientes servicios:

1. **backend** - Django API (puerto 8000)
2. **db** - PostgreSQL (puerto 5432)
3. **frontend** - Vue.js (puerto 80)
4. **nginx** - Proxy reverso (puertos 80/443)

### 5. Comandos de Despliegue

Coolify ejecutará automáticamente:

```bash
# Construir imágenes
docker-compose -f docker-compose.prod.yml build

# Desplegar servicios
docker-compose -f docker-compose.prod.yml up -d

# Ejecutar migraciones (primer despliegue)
docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate

# Crear superusuario (opcional)
docker-compose -f docker-compose.prod.yml exec backend python manage.py createsuperuser
```

### 6. Verificación del Despliegue

1. **Frontend**: https://nexusti.grupodecor.com
2. **API**: https://nexusti.grupodecor.com/api/
3. **Admin**: https://nexusti.grupodecor.com/admin/

### 7. Monitoreo y Logs

En Coolify podrás:
- Ver logs en tiempo real
- Monitorear recursos de contenedores
- Configurar alertas
- Hacer backups automáticos

### 8. Troubleshooting

#### Problemas Comunes:

1. **Error de conexión a base de datos**:
   - Verificar variables POSTGRES_*
   - Verificar que el contenedor db esté corriendo

2. **Error de CORS**:
   - Verificar DJANGO_ALLOWED_HOSTS
   - Verificar configuración de CORS en settings.py

3. **Error de SSL**:
   - Verificar configuración de dominio en Coolify
   - Verificar certificados SSL

4. **Error de LDAP**:
   - Verificar variables LDAP_*
   - Verificar conectividad al servidor LDAP

### 9. Backup y Recuperación

Coolify puede configurar:
- Backups automáticos de la base de datos
- Backups de archivos estáticos
- Restauración automática en caso de fallo

### 10. Escalabilidad

Para escalar la aplicación:
- Aumentar réplicas del backend
- Configurar load balancer
- Optimizar configuración de Nginx
- Implementar cache Redis

### 11. Seguridad

Recomendaciones:
- Cambiar contraseñas por defecto
- Configurar firewall
- Habilitar logs de seguridad
- Configurar monitoreo de intrusiones
- Mantener actualizadas las imágenes de Docker 