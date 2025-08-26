from django.shortcuts import render
from rest_framework import viewsets
from .models import Tip, Manual
from .serializers import TipSerializer, ManualSerializer
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

CACHE_TTL = 60 * 15

# Create your views here.

class TipViewSet(viewsets.ModelViewSet):
    queryset = Tip.objects.all()  # type: ignore
    serializer_class = TipSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class ManualViewSet(viewsets.ModelViewSet): 
    queryset = Manual.objects.all() # type: ignore
    serializer_class = ManualSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)