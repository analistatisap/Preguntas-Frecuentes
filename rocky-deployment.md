# 🚀 Guía de Despliegue en Rocky Linux - Pregúntame

## Configuración para Servidor Rocky Linux

### 📋 Información del Servidor

- **IP Pública**: 52.177.69.18
- **IP Privada**: 10.10.10.5
- **Sistema**: Rocky Linux
- **Dominio**: nexusti.grupodecor.com

### 🛠️ Preparación del Servidor Rocky Linux

#### Paso 1: Conectar al Servidor

```bash
# Conectar via SSH
ssh usuario@52.177.69.18

# Verificar sistema
cat /etc/os-release
```

#### Paso 2: Actualizar el Sistema

```bash
# Actualizar sistema
sudo dnf update -y

# Instalar herramientas básicas
sudo dnf install -y curl wget git vim net-tools
```

#### Paso 3: Instalar Docker (si no está instalado)

```bash
# Agregar repositorio de Docker
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# Instalar Docker
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Iniciar y habilitar Docker
sudo systemctl start docker
sudo systemctl enable docker

# Agregar usuario al grupo docker
sudo usermod -aG docker $USER

# Reiniciar sesión para aplicar cambios
newgrp docker
```

#### Paso 4: Instalar Docker Compose (si no está incluido)

```bash
# Instalar Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### 🚀 Despliegue de la Aplicación

#### Paso 1: Clonar el Repositorio

```bash
# Clonar el repositorio
git clone <tu-repositorio> preguntame
cd preguntame

# Dar permisos al script de despliegue
chmod +x deploy-rocky.sh
```

#### Paso 2: Configurar Firewall

```bash
# Instalar firewalld si no está instalado
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

# Verificar puertos abiertos
sudo firewall-cmd --list-ports
```

#### Paso 3: Ejecutar el Despliegue

```bash
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

### 🌐 Configuración de DNS

Configura el DNS para que `nexusti.grupodecor.com` apunte a `52.177.69.18`:

```
nexusti.grupodecor.com.  IN  A  52.177.69.18
```

### 📊 Verificación del Despliegue

#### URLs de Acceso

- **Frontend**: http://52.177.69.18
- **Frontend (IP privada)**: http://10.10.10.5
- **Backend API**: http://52.177.69.18:8000
- **Admin Django**: http://52.177.69.18:8000/admin/
- **Base de datos**: 52.177.69.18:5432

#### Comandos de Verificación

```bash
# Ver estado de contenedores
docker-compose -f docker-compose.rocky.yml ps

# Ver logs
docker-compose -f docker-compose.rocky.yml logs -f

# Ver logs de un servicio específico
docker-compose -f docker-compose.rocky.yml logs -f backend

# Verificar conectividad
curl -I http://localhost
curl -I http://52.177.69.18
```

### 🔍 Troubleshooting Específico para Rocky Linux

#### Problemas Comunes

1. **Error de permisos SELinux**:
   ```bash
   # Verificar estado de SELinux
   sestatus
   
   # Si está habilitado, configurar para Docker
   sudo setsebool -P container_manage_cgroup 1
   ```

2. **Puerto 80 ocupado por httpd**:
   ```bash
   # Detener httpd si está corriendo
   sudo systemctl stop httpd
   sudo systemctl disable httpd
   ```

3. **Error de memoria**:
   ```bash
   # Verificar memoria disponible
   free -h
   
   # Aumentar swap si es necesario
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   ```

4. **Error de red**:
   ```bash
   # Verificar interfaces de red
   ip addr show
   
   # Verificar conectividad
   ping -c 3 8.8.8.8
   ```

### 🛡️ Seguridad para Producción

#### Configurar SELinux (si está habilitado)

```bash
# Verificar estado
sestatus

# Si está habilitado, configurar para Docker
sudo setsebool -P container_manage_cgroup 1
sudo setsebool -P container_use_cgroup 1
```

#### Cambiar Contraseñas por Defecto

```bash
# Cambiar contraseña de PostgreSQL
docker-compose -f docker-compose.rocky.yml exec db psql -U preguntas -d preguntas_frecuentes -c "ALTER USER preguntas PASSWORD 'nueva_contraseña_segura';"

# Cambiar SECRET_KEY de Django
# Editar docker-compose.rocky.yml y cambiar SECRET_KEY
```

#### Configurar SSL/HTTPS

```bash
# Instalar Certbot
sudo dnf install -y certbot

# Obtener certificado SSL
sudo certbot certonly --standalone -d nexusti.grupodecor.com

# Configurar Nginx con SSL (crear configuración SSL)
```

### 📈 Monitoreo y Mantenimiento

#### Comandos Útiles

```bash
# Ver uso de recursos
docker stats

# Ver logs en tiempo real
docker-compose -f docker-compose.rocky.yml logs -f --tail=100

# Verificar espacio en disco
df -h

# Verificar uso de memoria
free -h

# Verificar procesos
ps aux | grep docker
```

#### Backup

```bash
# Backup de la base de datos
docker-compose -f docker-compose.rocky.yml exec db pg_dump -U preguntas preguntas_frecuentes > backup_$(date +%Y%m%d_%H%M%S).sql

# Backup de archivos estáticos
docker cp preguntame_backend:/app/staticfiles ./backup_static_$(date +%Y%m%d_%H%M%S)

# Backup de volúmenes Docker
docker run --rm -v preguntame_postgres_data:/data -v $(pwd):/backup alpine tar czf /backup/postgres_backup_$(date +%Y%m%d_%H%M%S).tar.gz -C /data .
```

### 🔄 Actualizaciones

```bash
# Actualizar código
git pull origin main

# Reconstruir y reiniciar
docker-compose -f docker-compose.rocky.yml down
docker-compose -f docker-compose.rocky.yml build --no-cache
docker-compose -f docker-compose.rocky.yml up -d

# Ejecutar migraciones si hay cambios en la base de datos
docker-compose -f docker-compose.rocky.yml exec backend python manage.py migrate
```

### 🚨 Comandos de Emergencia

```bash
# Detener todo
docker-compose -f docker-compose.rocky.yml down

# Reiniciar todo
docker-compose -f docker-compose.rocky.yml restart

# Ver logs de errores
docker-compose -f docker-compose.rocky.yml logs --tail=50 | grep ERROR

# Limpiar recursos no utilizados
docker system prune -f

# Reiniciar Docker
sudo systemctl restart docker
```

### 📞 Soporte

Si tienes problemas:

1. **Verificar logs**: `docker-compose -f docker-compose.rocky.yml logs -f`
2. **Verificar estado**: `docker-compose -f docker-compose.rocky.yml ps`
3. **Verificar conectividad**: `curl -I http://localhost`
4. **Verificar firewall**: `sudo firewall-cmd --list-ports`
5. **Verificar SELinux**: `sestatus`
6. **Reiniciar servicios**: `docker-compose -f docker-compose.rocky.yml restart`

### 🔧 Configuración Avanzada

#### Optimización de Rendimiento

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

#### Configuración de Logs

```bash
# Configurar rotación de logs
sudo tee /etc/logrotate.d/docker <<EOF
/var/lib/docker/containers/*/*.log {
    rotate 7
    daily
    compress
    size=1M
    missingok
    delaycompress
    copytruncate
}
EOF
``` 