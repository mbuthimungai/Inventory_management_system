from django.urls import path
from .views import *

urlpatterns = [
    path("update/<str:pk>", UpdateTransaction.as_view()),
    path("create", CreateTransaction.as_view()),
    path("one/<str:pk>", ReadTransactionByID.as_view()),
    path("", ReadTransactions.as_view()),
    path("delete/<str:pk>", DeleteTransaction.as_view())
]
