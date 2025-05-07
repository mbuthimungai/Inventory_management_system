from django.urls import path
from .views import (
   business_view
)
urlpatterns = [

    path("", business_view, name="get_business"),

]
