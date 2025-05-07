"""
URL configuration for inventory_management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('categories/', include('category_management.urls')),
        path("items/", include("item_management.urls")),
        path("stocks/", include("stock_management.urls")),
        path("suppliers/", include("supplier_management.urls")),
        path("transactions/", include("transaction_management.urls")),
        path("users/", include("auth_management.urls")),
        path("business/", include("business_management.urls")),
        # Include other app's URL configurations here, e.g.,
        # path('items/', include('item_management.urls')),
    ])),
]
