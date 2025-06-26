from django.db import models

# Create your models here.
from django.db import models

class Tip(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='tips/', blank=True, null=True)
    video = models.FileField(upload_to='tips/videos/', blank=True, null=True)
    video_url = models.CharField(max_length=500, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Manual(models.Model):
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='manuales/', blank=True, null=True)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo