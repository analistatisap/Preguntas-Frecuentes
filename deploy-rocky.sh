#!/bin/bash

# Script de despliegue para Rocky Linux - Pregúntame
# Uso: ./deploy-rocky.sh

set -e

echo "🚀 Iniciando despliegue en Rocky Linux..."

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para imprimir mensajes
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

# Verificar que estamos en Rocky Linux
if ! grep -q "Rocky" /etc/os-release; then
    print_warning "Este script está optimizado para Rocky Linux"
fi

# Verificar que Docker esté instalado
if ! command -v docker &> /dev/null; then
    print_error "Docker no está instalado. Instalando Docker..."
    
    # Instalar Docker en Rocky Linux
    sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker $USER
    
    print_status "Docker instalado. Por favor, reinicia la sesión y ejecuta el script nuevamente."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose no está instalado. Instalando..."
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

print_status "Docker y Docker Compose verificados ✅"

# Verificar conectividad de red
print_status "Verificando conectividad de red..."
if ping -c 1 8.8.8.8 &> /dev/null; then
    print_status "Conectividad a internet verificada ✅"
else
    print_warning "No se puede verificar conectividad a internet"
fi

# Verificar puertos disponibles
print_status "Verificando puertos disponibles..."
if sudo netstat -tlnp | grep :80 > /dev/null; then
    print_warning "Puerto 80 está en uso. Deteniendo servicio..."
    sudo systemctl stop httpd nginx apache2 2>/dev/null || true
fi

if sudo netstat -tlnp | grep :8000 > /dev/null; then
    print_warning "Puerto 8000 está en uso"
fi

# Detener contenedores existentes si los hay
print_status "Deteniendo contenedores existentes..."
docker-compose -f docker-compose.rocky.yml down --remove-orphans || true

# Limpiar imágenes antiguas (opcional)
read -p "¿Deseas limpiar imágenes Docker antiguas? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_status "Limpiando imágenes Docker..."
    docker system prune -f
fi

# Construir las imágenes
print_status "Construyendo imágenes Docker..."
docker-compose -f docker-compose.rocky.yml build --no-cache

# Levantar los servicios
print_status "Levantando servicios..."
docker-compose -f docker-compose.rocky.yml up -d

# Esperar a que los servicios estén listos
print_status "Esperando a que los servicios estén listos..."
sleep 45

# Verificar que los contenedores estén corriendo
print_status "Verificando estado de contenedores..."
docker-compose -f docker-compose.rocky.yml ps

# Ejecutar migraciones de Django
print_status "Ejecutando migraciones de Django..."
docker-compose -f docker-compose.rocky.yml exec -T backend python manage.py migrate

# Recolectar archivos estáticos
print_status "Recolectando archivos estáticos..."
docker-compose -f docker-compose.rocky.yml exec -T backend python manage.py collectstatic --noinput

# Crear superusuario (opcional)
read -p "¿Deseas crear un superusuario de Django? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_status "Creando superusuario..."
    docker-compose -f docker-compose.rocky.yml exec -T backend python manage.py createsuperuser
fi

# Verificar que todo esté funcionando
print_status "Verificando que los servicios estén funcionando..."

# Verificar backend
if curl -f http://localhost:8000/api/ > /dev/null 2>&1; then
    print_status "✅ Backend funcionando en http://localhost:8000"
else
    print_warning "⚠️  Backend no responde en http://localhost:8000"
fi

# Verificar frontend
if curl -f http://localhost:80 > /dev/null 2>&1; then
    print_status "✅ Frontend funcionando en http://localhost:80"
else
    print_warning "⚠️  Frontend no responde en http://localhost:80"
fi

# Verificar base de datos
if docker-compose -f docker-compose.rocky.yml exec -T db pg_isready -U preguntas > /dev/null 2>&1; then
    print_status "✅ Base de datos PostgreSQL funcionando"
else
    print_warning "⚠️  Base de datos no responde"
fi

# Verificar conectividad externa
print_status "Verificando conectividad externa..."
if curl -f http://52.177.69.18 > /dev/null 2>&1; then
    print_status "✅ Servicio accesible desde IP pública"
else
    print_warning "⚠️  Servicio no accesible desde IP pública"
fi

print_status "🎉 Despliegue completado!"

echo ""
echo "📋 URLs de acceso:"
echo "   - Frontend: http://52.177.69.18"
echo "   - Frontend (IP privada): http://10.10.10.5"
echo "   - Backend API: http://52.177.69.18:8000"
echo "   - Admin Django: http://52.177.69.18:8000/admin/"
echo "   - Base de datos: 52.177.69.18:5432"
echo ""

echo "🔧 Comandos útiles:"
echo "   - Ver logs: docker-compose -f docker-compose.rocky.yml logs -f"
echo "   - Detener: docker-compose -f docker-compose.rocky.yml down"
echo "   - Reiniciar: docker-compose -f docker-compose.rocky.yml restart"
echo "   - Ver estado: docker-compose -f docker-compose.rocky.yml ps"
echo ""

print_warning "⚠️  IMPORTANTE: Cambia las contraseñas por defecto en producción!"
print_warning "⚠️  IMPORTANTE: Configura SSL/HTTPS para producción!"
print_warning "⚠️  IMPORTANTE: Actualiza las variables de entorno con valores seguros!"

echo ""
print_status "Para acceder desde el dominio nexusti.grupodecor.com, asegúrate de:"
echo "   1. Configurar DNS para que apunte a 52.177.69.18"
echo "   2. Configurar el firewall para permitir puertos 80 y 8000"
echo "   3. Configurar SSL/HTTPS para producción"
echo ""

print_info "🔍 Información del servidor:"
echo "   - IP Pública: 52.177.69.18"
echo "   - IP Privada: 10.10.10.5"
echo "   - Sistema: Rocky Linux"
echo "   - Docker: $(docker --version)"
echo "   - Docker Compose: $(docker-compose --version)" 