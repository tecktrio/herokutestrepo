
from django.urls import path

import herokutest
from herokutestapp import views

urlpatterns = [

    path('', views.home),
    path('register', views.register),
    path('registerd', views.registerd),
    path('login', views.login),
    path('logedin', views.logedin),
    path('products', views.logedin),
    path('contact', views.logedin),
    path('about', views.logedin),
]