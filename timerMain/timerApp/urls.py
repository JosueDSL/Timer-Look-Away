from django.urls import path

from . import views

app_name = "timerApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("trial", views.trial, name="trial"),
    path("signup", views.signup, name="signup"),
    path("timers", views.timers, name="timers"),
    path("speech", views.speech, name="speech"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("password", views.password, name="password")
]