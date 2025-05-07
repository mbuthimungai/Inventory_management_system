from django.shortcuts import render
from rest_framework import generics
from django.views.generic import ListView
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

class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        # Filtrar categorías por el negocio del usuario autenticado
        business_id = self.request.GET.get('business_id')  # Supongamos que el negocio se pasa como parámetro
        return Category.objects.filter(business__owner=self.request.user, business_id=business_id)