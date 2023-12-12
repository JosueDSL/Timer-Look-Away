from django.urls import path

from . import views

app_name = "timerApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("trial/", views.trial, name="trial"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
]