from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_contact_email_task(nombre, apellido, correo_remitente, mensaje, destinatario):
    asunto = f'Nuevo mensaje de contacto de: {nombre} {apellido}'
    year = timezone.now().year
    html_content = render_to_string('contacto/correo_contacto.html', {
        'nombre': nombre,
        'apellido': apellido,
        'correo': correo_remitente,
        'mensaje': mensaje,
        'year': year
    })

    try:
        email = EmailMessage(
            asunto,
            html_content,
            settings.DEFAULT_FROM_EMAIL,
            [destinatario]
        )
        email.content_subtype = 'html'
        email.send(fail_silently=False)
        logger.info(f"Correo de contacto enviado exitosamente a {destinatario} desde {correo_remitente}")
        return True
    except Exception as e:
        logger.error(f"Error al enviar el correo de contacto: {str(e)}", exc_info=True)
        return False
