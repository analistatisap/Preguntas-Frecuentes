from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    """Serializer para validar las credenciales de login."""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)