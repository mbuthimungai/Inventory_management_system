from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from . import serializers
from .models import AuthUser as User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from datetime import timedelta

# Create your views here.
@api_view(['POST'])
def login_view(request):
    print(request.data)
    user = get_object_or_404(User, username=request.data.get('username'))
    if not user.check_password(request.data.get('password')):
        return Response({"error": "Invalid credentials"}, status=401)
    
    token, created = Token.objects.get_or_create(user=user)
    
    userSerializer = serializers.UserSerializer(instance=user)
    print(userSerializer)
    return Response({"token": token.key, "user":userSerializer.data}, status=200)


@api_view(['POST'])
def register_view(request):
    serializer = serializers.RegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({"error": serializer.errors}, status=400)
    
    # Aquí puedes manejar la lógica de registro, como crear un nuevo usuario
    # user = User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
    serializer.create(serializer.validated_data)
    
    try:
        # Aquí puedes manejar la lógica de registro, como crear un nuevo usuario
        user = User.objects.get(username=serializer.validated_data['username'])
        user.set_password(serializer.validated_data['password'])
        user.save()
        
        token = Token.objects.create(user=user)
        
        return Response({
            "message": "User registered successfully!",
            "token": token.key
        }, status=201)
        
    except Exception as e:
        return Response({"errorUser": str(e)}, status=400)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def my_profile_view(request):
    user = request.user
    userSerializer = serializers.UserSerializer(instance=user)
    token, created = Token.objects.get_or_create(user=user)
    if not user.is_authenticated:
        return Response({"error": "User not authenticated"}, status=401)
    
    # Aquí puedes devolver la información del perfil del usuario
    return Response({
        "user": userSerializer.data,
        "token": token.key,
    })