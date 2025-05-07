from rest_framework.serializers import ModelSerializer, ValidationError, ChoiceField, PrimaryKeyRelatedField
from .models import AuthUser as User
from business_management.models import Business

class LoginSerializer(ModelSerializer):
    """
    Serializer for the login view.
    """
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterSerializer(ModelSerializer):
    user_type = ChoiceField(choices=User.UserType.choices, required=True)
    client = PrimaryKeyRelatedField(
        queryset=User.objects.filter(user_type=User.UserType.CLIENT),
        required=False
    )
    business = PrimaryKeyRelatedField(
        queryset=Business.objects.all(),  # O filtrado si quieres
        required=False
    )

    class Meta:
        model = User
        fields = [
            'username', 'password', 'email',
            'first_name', 'last_name', 'phone',
            'identification_number', 'user_type',
            'client', 'business'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone': {'required': True},
            'identification_number': {'required': True},
        }

    def validate(self, data):
        if data['user_type'] == User.UserType.WORKER:
            client = data.get('client')
            business = data.get('business')
            if not client:
                raise ValidationError("Workers must be associated with a client.")
            if not business:
                raise ValidationError("Workers must be associated with a business.")
            if business.owner != client:
                raise ValidationError("The business must belong to the specified client.")
        return data


    def create(self, validated_data):
        client = validated_data.pop('client', None)
        business = validated_data.pop('business', None)
        user = User.objects.create_user(**validated_data)
        if client:
            user.client = client
        if business:
            user.business = business
        user.save()
        return user


class ClientSerializer(ModelSerializer):
    """
    Serializers
    """
    class Meta:
        model = User
        fields=["id", "first_name", "last_name"]

class BusinessSerializer(ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
        
class UserSerializer(ModelSerializer):
    """
    Serializer for the user profile view.
    """
    client =  ClientSerializer(read_only=True)
    business = BusinessSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'client', 'business']
        

    