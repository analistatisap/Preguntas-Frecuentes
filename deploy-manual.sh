#!/bin/bash

# Script de despliegue manual para Pregúntame
# Uso: ./deploy-manual.sh

set -e

echo "🚀 Iniciando despliegue manual de Pregúntame..."

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
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

# Verificar que Docker esté instalado
if ! command -v docker &> /dev/null; then
    print_error "Docker no está instalado. Por favor instala Docker primero."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose no está instalado. Por favor instala Docker Compose primero."
    exit 1
fi

print_status "Docker y Docker Compose verificados ✅"

# Detener contenedores existentes si los hay
print_status "Deteniendo contenedores existentes..."
docker-compose -f docker-compose.manual.yml down --remove-orphans || true

# Limpiar imágenes antiguas (opcional)
read -p "¿Deseas limpiar imágenes Docker antiguas? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_status "Limpiando imágenes Docker..."
    docker system prune -f
fi

# Construir las imágenes
print_status "Construyendo imágenes Docker..."
docker-compose -f docker-compose.manual.yml build --no-cache

# Levantar los servicios
print_status "Levantando servicios..."
docker-compose -f docker-compose.manual.yml up -d

# Esperar a que los servicios estén listos
print_status "Esperando a que los servicios estén listos..."
sleep 30

# Verificar que los contenedores estén corriendo
print_status "Verificando estado de contenedores..."
docker-compose -f docker-compose.manual.yml ps

# Ejecutar migraciones de Django
print_status "Ejecutando migraciones de Django..."
docker-compose -f docker-compose.manual.yml exec -T backend python manage.py migrate

# Recolectar archivos estáticos
print_status "Recolectando archivos estáticos..."
docker-compose -f docker-compose.manual.yml exec -T backend python manage.py collectstatic --noinput

# Crear superusuario (opcional)
read -p "¿Deseas crear un superusuario de Django? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_status "Creando superusuario..."
    docker-compose -f docker-compose.manual.yml exec -T backend python manage.py createsuperuser
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
if docker-compose -f docker-compose.manual.yml exec -T db pg_isready -U preguntas > /dev/null 2>&1; then
    print_status "✅ Base de datos PostgreSQL funcionando"
else
    print_warning "⚠️  Base de datos no responde"
fi

print_status "🎉 Despliegue completado!"

echo ""
echo "📋 URLs de acceso:"
echo "   - Frontend: http://localhost"
echo "   - Backend API: http://localhost:8000"
echo "   - Admin Django: http://localhost:8000/admin/"
echo "   - Base de datos: localhost:5432"
echo ""

echo "🔧 Comandos útiles:"
echo "   - Ver logs: docker-compose -f docker-compose.manual.yml logs -f"
echo "   - Detener: docker-compose -f docker-compose.manual.yml down"
echo "   - Reiniciar: docker-compose -f docker-compose.manual.yml restart"
echo "   - Ver estado: docker-compose -f docker-compose.manual.yml ps"
echo ""

print_warning "⚠️  IMPORTANTE: Cambia las contraseñas por defecto en producción!"
print_warning "⚠️  IMPORTANTE: Configura SSL/HTTPS para producción!"
print_warning "⚠️  IMPORTANTE: Actualiza las variables de entorno con valores seguros!"

echo ""
print_status "Para acceder desde el dominio nexusti.grupodecor.com, asegúrate de:"
echo "   1. Configurar DNS para que apunte a 52.177.69.18"
echo "   2. Configurar el firewall para permitir puertos 80 y 8000"
echo "   3. Configurar SSL/HTTPS para producción" 