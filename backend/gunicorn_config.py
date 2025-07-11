# Configuración de Gunicorn para producción
import multiprocessing

# Configuración del servidor
bind = "0.0.0.0:5048"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50

# Configuración de timeouts
timeout = 30
keepalive = 2
graceful_timeout = 30

# Configuración de logs
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Configuración de seguridad
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Configuración de preload
preload_app = True

# Configuración de worker
worker_tmp_dir = "/dev/shm"
worker_exit_on_app_exit = True

# Configuración de stats
statsd_host = None
statsd_prefix = "gunicorn"

# Configuración de SSL (si es necesario)
# keyfile = "/path/to/keyfile"
# certfile = "/path/to/certfile"

def when_ready(server):
    server.log.info("Servidor Gunicorn listo para recibir conexiones")

def worker_int(worker):
    worker.log.info("Worker recibió señal INT o QUIT")

def pre_fork(server, worker):
    server.log.info("Worker %s (pid: %s) iniciado", worker.age, worker.pid)

def post_fork(server, worker):
    server.log.info("Worker %s (pid: %s) creado", worker.age, worker.pid)

def post_worker_init(worker):
    worker.log.info("Worker %s (pid: %s) inicializado", worker.age, worker.pid)

def worker_abort(worker):
    worker.log.info("Worker %s (pid: %s) abortado", worker.age, worker.pid)