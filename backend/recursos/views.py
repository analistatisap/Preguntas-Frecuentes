from django.shortcuts import render
from rest_framework import viewsets
from .models import Tip, Manual
from .serializers import TipSerializer, ManualSerializer

# Create your views here.

class TipViewSet(viewsets.ModelViewSet):
    queryset = Tip.objects.all()  # type: ignore
    serializer_class = TipSerializer

class ManualViewSet(viewsets.ModelViewSet): 
    queryset = Manual.objects.all() # type: ignore
    serializer_class = ManualSerializer
