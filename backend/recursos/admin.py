from django.contrib import admin

admin.site.site_header = "Grupo Decor"
admin.site.site_title = "Grupo Decor"
admin.site.index_title = "Administración del sitio"

# Register your models here.
from django.contrib import admin
from .models import Tip, Manual

class TipAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion')
    fields = ('titulo', 'descripcion', 'imagen', 'video', 'video_url', 'fecha_creacion')
    readonly_fields = ('fecha_creacion',)

admin.site.register(Tip, TipAdmin)
admin.site.register(Manual)