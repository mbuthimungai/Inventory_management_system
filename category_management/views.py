from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
# Create your views here.

class ReadCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class UpdateCategory(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DeleteCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ReadCategoryByID(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"