from django.urls import path
from .views import *

urlpatterns = [
    path("update/<str:pk>", UpdateCategory.as_view()),
    path("", ReadCategory.as_view()),
    path("", CreateCategory.as_view()),
    path("delete/<str:pk>", DeleteCategory.as_view()),
    path("one/<str:pk>", ReadCategoryByID.as_view())
]
