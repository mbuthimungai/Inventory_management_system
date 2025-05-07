from rest_framework import serializers
from .models import Business

class BusinessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Business
        fields = '__all__'

class BusinessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True, 'allow_blank': False},
            'owner': {'required': False}
        }