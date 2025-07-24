# 🚀 Guía Completa de Despliegue - Pregúntame

## 📋 Índice

1. [Requisitos Previos](#requisitos-previos)
2. [Métodos de Despliegue](#métodos-de-despliegue)
   - [Despliegue con Coolify](#despliegue-con-coolify)
   - [Despliegue Manual](#despliegue-manual)
   - [Despliegue en Rocky Linux](#despliegue-en-rocky-linux)
3. [Configuración de Entorno](#configuración-de-entorno)
4. [Verificación y Monitoreo](#verificación-y-monitoreo)
5. [Troubleshooting](#troubleshooting)
6. [Seguridad](#seguridad)
7. [Mantenimiento](#mantenimiento)

---

## 📋 Requisitos Previos

### Software Necesario
- **Docker** (versión 20.10+)
- **Docker Compose** (versión 2.0+)
- **Git** para clonar el repositorio
- **Acceso SSH** al servidor (para despliegue manual)

### Información del Servidor
- **IP Pública**: `52.177.69.18`
- **IP Privada**: `10.10.10.5`
- **Dominio**: `nexusti.grupodecor.com`
- **Sistema**: Rocky Linux (para despliegue específico)

---

## 🚀 Métodos de Despliegue

### 1. Despliegue con Coolify (Recomendado)

#### Configuración en Coolify

1. **Crear Nueva Aplicación**
   - Accede a tu panel de Coolify
   - Crea una nueva aplicación
   - Nombre: `preguntame`
   - Tipo: `Docker Compose`

2. **Configurar Repositorio**
   - **URL del repositorio**: Tu repositorio Git
   - **Rama**: `main` o `master`
   - **Docker Compose File**: `docker-compose.prod.yml`

3. **Configurar Variables de Entorno**
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

4. **Configurar Dominio**
   - **Dominio**: `nexusti.grupodecor.com`
   - **IP Pública**: `52.177.69.18`
   - **SSL**: Habilitar (Coolify manejará los certificados)

#### URLs de Acceso (Coolify)
- **Frontend**: https://nexusti.grupodecor.com
- **API**: https://nexusti.grupodecor.com/api/
- **Admin**: https://nexusti.grupodecor.com/admin/

### 2. Despliegue Manual

#### Preparación del Servidor

```bash
# Conectar al servidor
ssh usuario@52.177.69.18

# Instalar Docker (si no está instalado)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Instalar Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Agregar usuario al grupo docker
sudo usermod -aG docker $USER
```

#### Despliegue

```bash
# Clonar el repositorio
git clone <tu-repositorio> preguntame
cd preguntame

# Dar permisos al script de despliegue
chmod +x deploy-manual.sh

# Ejecutar despliegue automático
./deploy-manual.sh
```

**O ejecutar manualmente:**
```bash
# Construir imágenes
docker-compose -f docker-compose.manual.yml build

# Levantar servicios
docker-compose -f docker-compose.manual.yml up -d

# Ejecutar migraciones
docker-compose -f docker-compose.manual.yml exec backend python manage.py migrate

# Recolectar archivos estáticos
docker-compose -f docker-compose.manual.yml exec backend python manage.py collectstatic --noinput

# Crear superusuario (opcional)
docker-compose -f docker-compose.manual.yml exec backend python manage.py createsuperuser
```

#### URLs de Acceso (Manual)
- **Frontend**: http://52.177.69.18
- **Backend API**: http://52.177.69.18:8000
- **Admin Django**: http://52.177.69.18:8000/admin/
- **Base de datos**: 52.177.69.18:5432

### 3. Despliegue en Rocky Linux

#### Preparación Específica para Rocky Linux

```bash
# Conectar via SSH
ssh usuario@52.177.69.18

# Actualizar sistema
sudo dnf update -y

# Instalar herramientas básicas
sudo dnf install -y curl wget git vim net-tools

# Instalar Docker
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Iniciar y habilitar Docker
sudo systemctl start docker
sudo systemctl enable docker

# Agregar usuario al grupo docker
sudo usermod -aG docker $USER
newgrp docker
```

#### Configurar Firewall (Rocky Linux)

```bash
# Instalar firewalld
sudo dnf install -y firewalld

# Iniciar y habilitar firewall
sudo systemctl start firewalld
sudo systemctl enable firewalld

# Permitir puertos necesarios
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-port=443/tcp
sudo firewall-cmd --permanent --add-port=8000/tcp
sudo firewall-cmd --permanent --add-port=5432/tcp

# Recargar firewall
sudo firewall-cmd --reload
```

#### Despliegue

```bash
# Clonar el repositorio
git clone <tu-repositorio> preguntame
cd preguntame

# Dar permisos al script de despliegue
chmod +x deploy-rocky.sh

# Ejecutar script de despliegue automático
./deploy-rocky.sh
```

**O ejecutar manualmente:**
```bash
# Construir imágenes
docker-compose -f docker-compose.rocky.yml build

# Levantar servicios
docker-compose -f docker-compose.rocky.yml up -d

# Ejecutar migraciones
docker-compose -f docker-compose.rocky.yml exec backend python manage.py migrate

# Recolectar archivos estáticos
docker-compose -f docker-compose.rocky.yml exec backend python manage.py collectstatic --noinput

# Crear superusuario (opcional)
docker-compose -f docker-compose.rocky.yml exec backend python manage.py createsuperuser
```

#### URLs de Acceso (Rocky Linux)
- **Frontend**: http://52.177.69.18
- **Frontend (IP privada)**: http://10.10.10.5
- **Backend API**: http://52.177.69.18:8000
- **Admin Django**: http://52.177.69.18:8000/admin/
- **Base de datos**: 52.177.69.18:5432

---

## ⚙️ Configuración de Entorno

### Variables de Entorno Comunes

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

# LDAP
LDAP_SERVER=tu_servidor_ldap
LDAP_PORT=389
LDAP_BIND_USER_DN=tu_usuario_ldap
LDAP_BIND_PASSWORD=tu_password_ldap
LDAP_BASE_DN=tu_base_dn_ldap
```

### Configuración de DNS

Configura el DNS para que `nexusti.grupodecor.com` apunte a `52.177.69.18`:

```
nexusti.grupodecor.com.  IN  A  52.177.69.18
```

---

## 📊 Verificación y Monitoreo

### Comandos de Verificación

```bash
# Ver estado de contenedores
docker-compose -f docker-compose.[tipo].yml ps

# Ver logs
docker-compose -f docker-compose.[tipo].yml logs -f

# Ver logs de un servicio específico
docker-compose -f docker-compose.[tipo].yml logs -f backend

# Verificar conectividad
curl -I http://localhost
curl -I http://52.177.69.18
```

### Monitoreo de Recursos

```bash
# Ver uso de recursos
docker stats

# Ver logs en tiempo real
docker-compose -f docker-compose.[tipo].yml logs -f --tail=100

# Verificar espacio en disco
df -h

# Verificar uso de memoria
free -h
```

---

## 🔍 Troubleshooting

### Problemas Comunes

#### 1. Puerto 80 ocupado
```bash
# Ver qué está usando el puerto 80
sudo netstat -tlnp | grep :80

# Detener servicio que use el puerto
sudo systemctl stop apache2  # o nginx
```

#### 2. Error de permisos Docker
```bash
# Reiniciar sesión después de agregar usuario al grupo docker
newgrp docker
```

#### 3. Error de memoria
```bash
# Verificar memoria disponible
free -h

# Aumentar swap si es necesario (Rocky Linux)
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

#### 4. Error de base de datos
```bash
# Verificar logs de la base de datos
docker-compose -f docker-compose.[tipo].yml logs db

# Reiniciar solo la base de datos
docker-compose -f docker-compose.[tipo].yml restart db
```

#### 5. Error de permisos SELinux (Rocky Linux)
```bash
# Verificar estado de SELinux
sestatus

# Si está habilitado, configurar para Docker
sudo setsebool -P container_manage_cgroup 1
sudo setsebool -P container_use_cgroup 1
```

#### 6. Error de CORS
- Verificar `DJANGO_ALLOWED_HOSTS`
- Verificar configuración de CORS en `settings.py`

#### 7. Error de SSL
- Verificar configuración de dominio
- Verificar certificados SSL

#### 8. Error de LDAP
- Verificar variables `LDAP_*`
- Verificar conectividad al servidor LDAP

---

## 🛡️ Seguridad

### Cambiar Contraseñas por Defecto

```bash
# Cambiar contraseña de PostgreSQL
docker-compose -f docker-compose.[tipo].yml exec db psql -U preguntas -d preguntas_frecuentes -c "ALTER USER preguntas PASSWORD 'nueva_contraseña_segura';"

# Cambiar SECRET_KEY de Django
# Editar docker-compose.[tipo].yml y cambiar SECRET_KEY
```

### Configurar SSL/HTTPS

```bash
# Instalar Certbot
sudo apt update  # Ubuntu/Debian
sudo apt install certbot

# O Rocky Linux
sudo dnf install -y certbot

# Obtener certificado SSL
sudo certbot certonly --standalone -d nexusti.grupodecor.com
```

### Configuración de Firewall

```bash
# Ubuntu/Debian
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 8000/tcp
sudo ufw allow 5432/tcp
sudo ufw enable

# Rocky Linux
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-port=443/tcp
sudo firewall-cmd --permanent --add-port=8000/tcp
sudo firewall-cmd --permanent --add-port=5432/tcp
sudo firewall-cmd --reload
```

---

## 🔄 Mantenimiento

### Backup

```bash
# Backup de la base de datos
docker-compose -f docker-compose.[tipo].yml exec db pg_dump -U preguntas preguntas_frecuentes > backup_$(date +%Y%m%d_%H%M%S).sql

# Backup de archivos estáticos
docker cp preguntame_backend:/app/staticfiles ./backup_static_$(date +%Y%m%d_%H%M%S)

# Backup de volúmenes Docker
docker run --rm -v preguntame_postgres_data:/data -v $(pwd):/backup alpine tar czf /backup/postgres_backup_$(date +%Y%m%d_%H%M%S).tar.gz -C /data .
```

### Actualizaciones

```bash
# Actualizar código
git pull origin main

# Reconstruir y reiniciar
docker-compose -f docker-compose.[tipo].yml down
docker-compose -f docker-compose.[tipo].yml build --no-cache
docker-compose -f docker-compose.[tipo].yml up -d

# Ejecutar migraciones si hay cambios en la base de datos
docker-compose -f docker-compose.[tipo].yml exec backend python manage.py migrate
```

### Comandos de Emergencia

```bash
# Detener todo
docker-compose -f docker-compose.[tipo].yml down

# Reiniciar todo
docker-compose -f docker-compose.[tipo].yml restart

# Ver logs de errores
docker-compose -f docker-compose.[tipo].yml logs --tail=50 | grep ERROR

# Limpiar recursos no utilizados
docker system prune -f

# Reiniciar Docker
sudo systemctl restart docker
```

### Optimización de Rendimiento

```bash
# Configurar límites de memoria para Docker
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<EOF
{
  "storage-driver": "overlay2",
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
EOF

# Reiniciar Docker
sudo systemctl restart docker
```

---

## 📞 Soporte

Si tienes problemas:

1. **Verificar logs**: `docker-compose -f docker-compose.[tipo].yml logs -f`
2. **Verificar estado**: `docker-compose -f docker-compose.[tipo].yml ps`
3. **Verificar conectividad**: `curl -I http://localhost`
4. **Verificar firewall**: `sudo firewall-cmd --list-ports` (Rocky Linux)
5. **Verificar SELinux**: `sestatus` (Rocky Linux)
6. **Reiniciar servicios**: `docker-compose -f docker-compose.[tipo].yml restart`

---

## 📝 Notas

- Reemplaza `[tipo]` con `prod`, `manual`, o `rocky` según el método de despliegue
- Los archivos de configuración específicos son:
  - Coolify: `docker-compose.prod.yml`
  - Manual: `docker-compose.manual.yml`
  - Rocky Linux: `docker-compose.rocky.yml`
- Siempre haz backup antes de actualizaciones importantes
- Mantén las contraseñas seguras y actualizadas
- Monitorea regularmente los logs y recursos del sistema 