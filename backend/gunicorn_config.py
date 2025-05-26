# Archivo de configuración para Gunicorn

bind = "0.0.0.0:8000" # Escucha en todas las interfaces en el puerto 8000
# Ajusta el número de workers según los núcleos de CPU de tu servidor
# Una buena regla general es (2 * número_de_cores) + 1
workers = 3 # Puedes ajustar este valor
accesslog = "-"  # Enviar logs de acceso a stdout (para que Podman los recoja)
errorlog = "-"   # Enviar logs de error a stderr (para que Podman los recoja)
loglevel = "info" # Nivel de detalle de los logs