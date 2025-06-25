from django.shortcuts import render
from rest_framework import viewsets
from .models import Tip, Manual
from .serializers import TipSerializer, ManualSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class TipViewSet(viewsets.ModelViewSet):
    queryset = Tip.objects.all()  # type: ignore
    serializer_class = TipSerializer
    permission_classes = [AllowAny]

class ManualViewSet(viewsets.ModelViewSet): 
    queryset = Manual.objects.all() # type: ignore
    serializer_class = ManualSerializer
    permission_classes = [AllowAny]
