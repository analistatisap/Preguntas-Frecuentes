from django.urls import path
from . import views # Importa las vistas de la aplicación actual

urlpatterns = [
    path('enviar-correo/', views.enviar_correo_api, name='api_enviar_correo'),
    # El nombre 'api_enviar_correo' es opcional pero útil.
    # La URL completa será algo como /api/tu_app/enviar-correo/ dependiendo de cómo lo configures en el urls.py del proyecto.
]
