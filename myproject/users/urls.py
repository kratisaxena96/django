from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),  #localhost/users/
    path("home/",views.home),  #localhost/users/home
    path("signin/",views.login),  #localhost/users/signin --> /users/signin
]