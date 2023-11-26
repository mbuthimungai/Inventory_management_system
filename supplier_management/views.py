from django.shortcuts import render
from rest_framework import generics
from .models import Supplier
from .serializers import SupplierSerializer
# Create your views here.

class ReadSuppliers(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class UpdateSupplier(generics.RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CreateSupplier(generics.CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class DeleteSupplier(generics.DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class ReadSupplierByID(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = "pk"