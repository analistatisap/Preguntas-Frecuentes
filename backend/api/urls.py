from django.urls import path
from . import views
from .views import UserProfileView
from Preguntas_frecuentes.views import LoginAPIView

urlpatterns = [
    # Ruta para la autenticación LDAP y JWT
    path('login/', LoginAPIView.as_view(), name='login_jwt'),
    # Rutas para los otros endpoints  en views.py
    path('enviar-correo/', views.enviar_correo_view, name='enviar_correo'),
    path('manuales/', views.obtener_manuales_view, name='obtener_manuales'),
    path('tips/', views.obtener_tips_view, name='obtener_tips'),
    path('user/', UserProfileView.as_view(), name='user-profile'),
]