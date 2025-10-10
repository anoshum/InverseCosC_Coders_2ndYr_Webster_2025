from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.Landing,name='Landing'),
    path('new', views.File_new,name='New_complain'),
    path('register', views.Sign_Up,name='New_User'),
    path('dashboard', views.Dash,name='Dashboard'),
    path('dmn', views.admin_page,name='dmn'),
    path('work',views.worker,name='worker'),
    path('sc',views.F_n,name='subc'),
    
]
