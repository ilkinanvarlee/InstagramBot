from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("", views.index, name="index"),

    path("instagram/", views.instagram, name="instagram"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),

]

