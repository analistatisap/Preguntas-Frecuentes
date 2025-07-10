# 🚀 Guía de Despliegue Manual - Pregúntame

## Configuración para Despliegue Manual con Contenedores

### 📋 Requisitos Previos

1. **Docker** instalado
2. **Docker Compose** instalado
3. **Git** para clonar el repositorio
4. **Acceso al servidor** con IP `52.177.69.18`

### 🛠️ Pasos de Despliegue

#### Paso 1: Preparar el Servidor

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

#### Paso 2: Clonar y Preparar el Proyecto

```bash
# Clonar el repositorio
git clone <tu-repositorio> preguntame
cd preguntame

# Dar permisos al script de despliegue
chmod +x deploy-manual.sh
```

#### Paso 3: Configurar Variables de Entorno (Opcional)

Si quieres personalizar las variables, edita `docker-compose.manual.yml`:

```yaml
environment:
  - SECRET_KEY=tu_clave_secreta_aqui
  - POSTGRES_PASSWORD=tu_password_seguro
  - LDAP_SERVER=tu_servidor_ldap
  # ... otras variables
```

#### Paso 4: Ejecutar el Despliegue

```bash
# Ejecutar el script de despliegue automático
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

### 🌐 Configuración de DNS

Configura el DNS para que `nexusti.grupodecor.com` apunte a `52.177.69.18`:

```
nexusti.grupodecor.com.  IN  A  52.177.69.18
```

### 🔧 Configuración del Firewall

```bash
# Permitir puertos necesarios
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 8000/tcp
sudo ufw allow 5432/tcp

# Habilitar firewall
sudo ufw enable
```

### 📊 Verificación del Despliegue

#### Verificar Servicios

```bash
# Ver estado de contenedores
docker-compose -f docker-compose.manual.yml ps

# Ver logs
docker-compose -f docker-compose.manual.yml logs -f

# Ver logs de un servicio específico
docker-compose -f docker-compose.manual.yml logs -f backend
```

#### URLs de Acceso

- **Frontend**: http://52.177.69.18 o http://nexusti.grupodecor.com
- **Backend API**: http://52.177.69.18:8000
- **Admin Django**: http://52.177.69.18:8000/admin/
- **Base de datos**: 52.177.69.18:5432

### 🔍 Troubleshooting

#### Problemas Comunes

1. **Puerto 80 ocupado**:
   ```bash
   # Ver qué está usando el puerto 80
   sudo netstat -tlnp | grep :80
   
   # Detener servicio que use el puerto
   sudo systemctl stop apache2  # o nginx
   ```

2. **Error de permisos Docker**:
   ```bash
   # Reiniciar sesión después de agregar usuario al grupo docker
   newgrp docker
   ```

3. **Error de memoria**:
   ```bash
   # Aumentar memoria disponible para Docker
   sudo systemctl stop docker
   sudo dockerd --storage-driver=overlay2 --storage-opt overlay2.size=10G
   ```

4. **Error de base de datos**:
   ```bash
   # Verificar logs de la base de datos
   docker-compose -f docker-compose.manual.yml logs db
   
   # Reiniciar solo la base de datos
   docker-compose -f docker-compose.manual.yml restart db
   ```

### 🛡️ Seguridad para Producción

#### Cambiar Contraseñas por Defecto

```bash
# Cambiar contraseña de PostgreSQL
docker-compose -f docker-compose.manual.yml exec db psql -U preguntas -d preguntas_frecuentes -c "ALTER USER preguntas PASSWORD 'nueva_contraseña_segura';"

# Cambiar SECRET_KEY de Django
# Editar docker-compose.manual.yml y cambiar SECRET_KEY
```

#### Configurar SSL/HTTPS

```bash
# Instalar Certbot
sudo apt update
sudo apt install certbot

# Obtener certificado SSL
sudo certbot certonly --standalone -d nexusti.grupodecor.com

# Configurar Nginx con SSL (crear configuración SSL)
```

### 📈 Monitoreo

#### Comandos Útiles

```bash
# Ver uso de recursos
docker stats

# Ver logs en tiempo real
docker-compose -f docker-compose.manual.yml logs -f --tail=100

# Ver logs de un servicio específico
docker-compose -f docker-compose.manual.yml logs -f backend

# Verificar conectividad
curl -I http://localhost
curl -I http://localhost:8000/api/
```

#### Backup

```bash
# Backup de la base de datos
docker-compose -f docker-compose.manual.yml exec db pg_dump -U preguntas preguntas_frecuentes > backup_$(date +%Y%m%d_%H%M%S).sql

# Backup de archivos estáticos
docker cp preguntame_backend:/app/staticfiles ./backup_static_$(date +%Y%m%d_%H%M%S)
```

### 🔄 Actualizaciones

```bash
# Actualizar código
git pull origin main

# Reconstruir y reiniciar
docker-compose -f docker-compose.manual.yml down
docker-compose -f docker-compose.manual.yml build --no-cache
docker-compose -f docker-compose.manual.yml up -d

# Ejecutar migraciones si hay cambios en la base de datos
docker-compose -f docker-compose.manual.yml exec backend python manage.py migrate
```

### 🚨 Comandos de Emergencia

```bash
# Detener todo
docker-compose -f docker-compose.manual.yml down

# Reiniciar todo
docker-compose -f docker-compose.manual.yml restart

# Ver logs de errores
docker-compose -f docker-compose.manual.yml logs --tail=50 | grep ERROR

# Limpiar recursos no utilizados
docker system prune -f
```

### 📞 Soporte

Si tienes problemas:

1. **Verificar logs**: `docker-compose -f docker-compose.manual.yml logs -f`
2. **Verificar estado**: `docker-compose -f docker-compose.manual.yml ps`
3. **Verificar conectividad**: `curl -I http://localhost`
4. **Revisar configuración**: Verificar `docker-compose.manual.yml`
5. **Reiniciar servicios**: `docker-compose -f docker-compose.manual.yml restart` 