import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # Para simplificar en desarrollo, ¡cuidado en producción!
from django.core.mail import send_mail
from django.conf import settings # Para acceder a la configuración del correo

@csrf_exempt 
def enviar_correo_api(request):
    if request.method == 'POST':
        try:
            # Cargar los datos JSON del cuerpo de la solicitud
            data = json.loads(request.body)
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            correo_remitente = data.get('correo') # El correo de la persona que llena el formulario
            mensaje = data.get('mensaje')
            destinatario = data.get('destinatario') # El correo al que se enviará (jagrajales@grupodecor.com)

            if not all([nombre, apellido, correo_remitente, mensaje, destinatario]):
                return JsonResponse({'error': 'Faltan datos en la solicitud'}, status=400)

            # Construir el asunto y el cuerpo del correo
            asunto = f'Nuevo mensaje de contacto de: {nombre} {apellido}'
            cuerpo_mensaje = f"""
            Has recibido un nuevo mensaje de contacto:

            Nombre: {nombre} {apellido}
            Correo Remitente: {correo_remitente}

            Mensaje:
            {mensaje}
            """

            send_mail(
                asunto,
                cuerpo_mensaje,
                settings.DEFAULT_FROM_EMAIL, # El correo desde el que Django enviará (configurado en settings.py)
                [destinatario],
                fail_silently=False,
            )

            return JsonResponse({'message': 'Correo enviado exitosamente'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except Exception as e:
            # En producción, sería bueno loggear este error 'e'
            return JsonResponse({'error': f'Ocurrió un error al enviar el correo: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

