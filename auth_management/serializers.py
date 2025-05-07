from rest_framework.serializers import ModelSerializer, ValidationError
from .models import AuthUser as User

class LoginSerializer(ModelSerializer):
    """
    Serializer for the login view.
    """
    class Meta:
        model = User
        fields = ['username', 'password']
from rest_framework import serializers
from .models import AuthUser as User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'password', 'email',
            'first_name', 'last_name', 'phone', 'identification_number'
        ]
        extra_kwargs = {
            'password': {'write_only': True},  # ✅ CORRECTO
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone': {'required': True},
            'identification_number': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(ModelSerializer):
    """
    Serializer for the user profile view.
    """
    class Meta:
        model = User
        fields = ['id','username', 'email', 'first_name', 'last_name']