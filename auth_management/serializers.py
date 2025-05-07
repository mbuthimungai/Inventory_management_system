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
    user_type = serializers.ChoiceField(choices=User.UserType.choices, required=True)
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(user_type=User.UserType.CLIENT), required=False)

    class Meta:
        model = User
        fields = [
            'username', 'password', 'email',
            'first_name', 'last_name', 'phone', 'identification_number', 'user_type', 'client'
        ]
        extra_kwargs = {
            'password': {'write_only': True},  # ✅ CORRECTO
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone': {'required': True},
            'identification_number': {'required': True},
        }

    def validate(self, data):
        if data['user_type'] == User.UserType.WORKER and not data.get('client'):
            raise ValidationError("Workers must be associated with a client.")
        return data

    def create(self, validated_data):
        client = validated_data.pop('client', None)
        user = User.objects.create_user(**validated_data)
        if client:
            user.client = client
            user.save()
        return user

class ClientSerializer(ModelSerializer):
    """
    Serializers
    """
    class Meta:
        model = User
        fields=["id", "first_name", "last_name"]
class UserSerializer(ModelSerializer):
    """
    Serializer for the user profile view.
    """
    client =  ClientSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'client']
        

    