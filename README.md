# Pregúntame - Sistema de Preguntas Frecuentes

Aplicación web para gestión de preguntas frecuentes con autenticación LDAP y chatbot inteligente.

## 🚀 Despliegue en Coolify

### Configuración Rápida

1. **Clona el repositorio** en tu servidor Coolify
2. **Configura las variables de entorno** (ver `env.example`)
3. **Configura el dominio**: `nexusti.grupodecor.com`
4. **Despliega** usando `docker-compose.prod.yml`

### Estructura de Servicios

- **Backend**: Django API (puerto 8000)
- **Frontend**: Vue.js (puerto 80)
- **Base de datos**: PostgreSQL (puerto 5432)
- **Proxy**: Nginx (puertos 80/443)

### URLs de Acceso

- **Aplicación**: https://nexusti.grupodecor.com
- **API**: https://nexusti.grupodecor.com/api/
- **Admin**: https://nexusti.grupodecor.com/admin/

## 📋 Requisitos

- Docker y Docker Compose
- Coolify instalado
- Dominio configurado
- Servidor LDAP (opcional)

## 🔧 Configuración

### Variables de Entorno Requeridas

```bash
# Django
SECRET_KEY=tu_clave_secreta
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=nexusti.grupodecor.com,52.177.69.18

# Base de datos
POSTGRES_DB=preguntas_frecuentes
POSTGRES_USER=preguntas
POSTGRES_PASSWORD=contraseña_segura

# Email
EMAIL_HOST=smtp.office365.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu_email
EMAIL_HOST_PASSWORD=tu_password

# LDAP (opcional)
LDAP_SERVER=tu_servidor_ldap
LDAP_PORT=389
LDAP_BIND_USER_DN=tu_usuario
LDAP_BIND_PASSWORD=tu_password
LDAP_BASE_DN=tu_base_dn
```

## 🛠️ Desarrollo Local

```bash
# Clonar repositorio
git clone <tu-repositorio>

# Configurar variables de entorno
cp env.example .env
# Editar .env con tus valores

# Ejecutar con Docker Compose
docker-compose up -d

# Ejecutar migraciones
docker-compose exec backend python manage.py migrate

# Crear superusuario
docker-compose exec backend python manage.py createsuperuser
```

## 📁 Estructura del Proyecto

```
Preguntas-Frecuentes/
├── backend/                 # API Django
│   ├── Preguntas_frecuentes/
│   ├── recursos/
│   ├── contacto/
│   └── Containerfile
├── frontend/               # Frontend Vue.js
│   └── preguntas_frecuentes/
│       └── Containerfile
├── nginx/                  # Configuración Nginx
├── docker-compose.prod.yml # Configuración producción
└── coolify-deployment.md   # Guía de despliegue
```

## 🔒 Seguridad

- SSL/TLS habilitado
- Headers de seguridad configurados
- Autenticación LDAP
- CORS configurado
- Rate limiting disponible

## 📊 Monitoreo

- Logs en tiempo real
- Métricas de contenedores
- Alertas configurables
- Backups automáticos

## 🆘 Soporte

Para problemas de despliegue, consulta:
1. `coolify-deployment.md` - Guía completa
2. Logs de Coolify
3. Configuración de DNS
4. Variables de entorno

## 📝 Licencia

Este proyecto es propiedad de Grupo Decor. 