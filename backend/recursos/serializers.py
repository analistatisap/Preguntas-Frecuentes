from rest_framework import serializers
from .models import Tip, Manual

class TipSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(use_url=True, required=False, allow_null=True)
    class Meta:
        model = Tip
        fields = '__all__'

class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = '__all__'
