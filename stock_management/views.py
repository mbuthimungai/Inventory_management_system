from django.shortcuts import render
from rest_framework import generics
from .models import Stock
from .serializers import StockSerializer
# Create your views here.

class ReadStocks(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
class UpdateStock(generics.RetrieveUpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class CreateStock(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
class DeleteStock(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class ReadStockByID(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "pk"
    