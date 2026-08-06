from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("upload/", views.upload, name="upload"),

    path("upload/", views.upload_video, name="upload"),
    path("projects/", views.projects, name="projects"),
]