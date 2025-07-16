import json
import re
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.utils import timezone




# Configura el logger
logger = logging.getLogger(__name__)

@csrf_exempt  # En producción, considera usar un token CSRF en lugar de eximirlo
def enviar_correo_api(request):
    if request.method == 'POST':
        try:
            # Cargar los datos JSON del cuerpo de la solicitud
            data = json.loads(request.body)
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            correo_remitente = data.get('correo')  # El correo de la persona que llena el formulario
            mensaje = data.get('mensaje')
            destinatario = "SOPORTEMAS@ITAAS.NET.CO"  # El correo al que se enviará (fijo)

            # Validar que todos los campos estén presentes
            if not all([nombre, apellido, correo_remitente, mensaje]):
                return JsonResponse({'error': 'Faltan datos en la solicitud'}, status=400)

            # Validar el formato del correo electrónico
            if not re.match(r"[^@]+@[^@]+\.[^@]+", correo_remitente):
                return JsonResponse({'error': 'El correo remitente no tiene un formato válido'}, status=400)

            # Construir el asunto
            asunto = f'Nuevo mensaje de contacto de: {nombre} {apellido}'

            # Renderizar la plantilla HTML
            year = timezone.now().year
            html_content = render_to_string('contacto/correo_contacto.html', {
                'nombre': nombre,
                'apellido': apellido,
                'correo': correo_remitente,
                'mensaje': mensaje,
                'year': year
            })

            # Intentar enviar el correo en HTML
            try:
                email = EmailMessage(
                    asunto,
                    html_content,
                    settings.DEFAULT_FROM_EMAIL,
                    [destinatario]
                )
                email.content_subtype = 'html'  # Importante para que se envíe como HTML
                email.send(fail_silently=False)
            except BadHeaderError:
                return JsonResponse({'error': 'Encabezado de correo inválido'}, status=400)

            return JsonResponse({'message': 'Correo enviado exitosamente'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except Exception as e:
            # Loguear el error para depuración
            logger.error(f"Error al enviar el correo: {str(e)}")
            return JsonResponse({'error': 'Ocurrió un error al enviar el correo'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': user.username
            }, status=status.HTTP_200_OK)

        return Response({"detail": "Credenciales inválidas o usuario no encontrado en AD."}, status=status.HTTP_401_UNAUTHORIZED)