from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home , name="signup"),
    path('login', views.login, name="login"),
    path('newUser', views.newUser, name="newUser"),
    path('userLogin', views.userLogin, name="userLogin")
    
]