from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.Landing,name='Landing'),
    path('new', views.File_new,name='New_complain'),
    path('register', views.Sign_Up,name='New_User'),
    path('dashboard', views.Dash,name='Dashboard'),
    
]
