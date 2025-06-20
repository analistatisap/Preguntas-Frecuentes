from django.urls import path
from . import views # Importa las vistas de la aplicación actual
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('enviar-correo/', views.enviar_correo_api, name='api_enviar_correo'),
    path('api/login/', views.LoginView.as_view(), name='api_login'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]
