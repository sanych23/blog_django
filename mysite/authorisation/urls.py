from django.contrib import admin
from django.urls import path

from .views import Auth


urlpatterns = [
    path("login/", Auth.login),
    path("login-form/", Auth.loginform, name="login"),
    path("registration/", Auth.registration),
    path("registration-form/", Auth.registrationform, name="register"),
]
