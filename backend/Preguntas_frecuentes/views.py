from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer # Importa el nuevo serializer
import logging
from rest_framework_simplejwt.tokens import RefreshToken

# Obtener una instancia del logger
logger = logging.getLogger(__name__)

def home(request):
    """Vista simple para la página de inicio."""
    return HttpResponse("<h1>Bienvenido a la página de inicio</h1>".encode("utf-8"))

class LoginAPIView(APIView):
    """
    API para el inicio de sesión de usuarios.
    Recibe username y password, y devuelve un JWT si el usuario es válido y activo.
    """
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']  # type: ignore
            password = serializer.validated_data['password']  # type: ignore
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                        'user': {
                            'username': user.username,
                            'first_name': user.first_name,
                            'last_name': user.last_name,
                            'email': user.email,
                        }
                    }, status=status.HTTP_200_OK)
                else:
                    logger.warning(f"Usuario inactivo: {username}")
                    return Response({'detail': 'La cuenta está inactiva o bloqueada.'}, status=status.HTTP_403_FORBIDDEN)
            else:
                logger.warning(f"Intento de login fallido para el usuario: {username}")
                return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            logger.error(f"Error de validación en el login: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)