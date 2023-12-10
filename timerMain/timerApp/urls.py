from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("josue", views.josue, name="josue"),
]