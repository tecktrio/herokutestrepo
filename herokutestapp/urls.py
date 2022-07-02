
from django.urls import path

import herokutest
from herokutestapp import views

urlpatterns = [

    path('', views.home),
    path('register', views.register),
    path('registerd', views.registerd),
]