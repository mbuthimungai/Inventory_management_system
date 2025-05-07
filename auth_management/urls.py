from django.urls import re_path
from . import views
urlpatterns = [
    # URL para el inicio de sesión
    re_path("login/", view=views.login_view, name="login"),
    re_path("register/", view=views.register_view, name="register"),
    re_path("profile/", view=views.my_profile_view, name="my_profile"),  # URL para el perfil del usuario
]
