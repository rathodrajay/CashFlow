from django.urls import path
from .import views as v
urlpatterns = [
    path("Register",v.addUser,name="reg"),
    path("Login",v.checkuser,name="log"),
    path("Logout",v.lgot,name="logout")
]