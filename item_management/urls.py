from django.urls import path
from .views import *

urlpatterns = [
    path("update/<str:pk>", UpdateItem.as_view()),
    path("", ReadItem.as_view()),
    path("", CreateItem.as_view()),
    path("delete/<str:pk>", DeleteItem.as_view()),
    path("one/<str:pk>", ReadItemByID.as_view())
]
