from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
# Create your views here.

class ReadItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UpdateItem(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CreateItem(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class DeleteItem(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ReadItemByID(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "pk"