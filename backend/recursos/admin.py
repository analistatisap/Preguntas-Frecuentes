from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tip, Manual

admin.site.register(Tip)
admin.site.register(Manual)