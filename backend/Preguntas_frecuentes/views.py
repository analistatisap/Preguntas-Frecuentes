from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer # Importa el nuevo serializer
import logging
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

# Obtener una instancia del logger
logger = logging.getLogger(__name__)

def home(request):
    """Vista simple para la página de inicio."""
    return HttpResponse("<h1>Bienvenido a la página de inicio</h1>".encode("utf-8"))

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    """
    API para el inicio de sesión de usuarios.
    Recibe username y password, y devuelve un token de autenticación.
    """
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']  # type: ignore
            password = serializer.validated_data['password']  # type: ignore
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # El usuario es autenticado, obtener o crear el token
                token, created = Token.objects.get_or_create(user=user)  # type: ignore
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                logger.warning(f"Intento de login fallido para el usuario: {username}")
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            logger.error(f"Error de validación en el login: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)