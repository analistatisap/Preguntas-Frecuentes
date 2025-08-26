#!/bin/sh
# Este script se ejecuta cuando el contenedor se inicie.

echo "Verificando que gunicorn_config.py exista..."
if [ -f "/app/gunicorn_config.py" ]; then
    echo "gunicorn_config.py encontrado."
else
    echo "ERROR: gunicorn_config.py NO ENCONTRADO."
    exit 1
fi

echo "Iniciando Gunicorn..."
exec gunicorn --config gunicorn_config.py Preguntas_frecuentes.wsgi:application