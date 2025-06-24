from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la autenticación LDAP
    path('login/', views.login_ldap_view, name='login_ldap'),
    # Rutas para los otros endpoints que tienes en views.py
    path('enviar-correo/', views.enviar_correo_view, name='enviar_correo'),
    path('manuales/', views.obtener_manuales_view, name='obtener_manuales'),
        path('tips/', views.obtener_tips_view, name='obtener_tips'),
]