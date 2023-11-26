from django.urls import path
from .views import *
urlpatterns = [
    path("update/<str:pk>", UpdateSupplier.as_view()),
    path("", ReadSuppliers.as_view()),
    path("delete/<str:pk>", DeleteSupplier.as_view()),
    path("one/<str:pk>", ReadSupplierByID.as_view()),
    path("create", CreateSupplier.as_view())
]
