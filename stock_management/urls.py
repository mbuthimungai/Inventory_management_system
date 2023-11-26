from django.urls import path
from .views import *

urlpatterns = [
    path("update/<str:pk>", UpdateStock.as_view()),
    path("", ReadStocks.as_view()),
    path("create", CreateStock.as_view()),
    path("delete/<str:pk>", DeleteStock.as_view()),
    path("one/<str:pk>", ReadStockByID.as_view())
]
