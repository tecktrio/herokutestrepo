
from django.urls import path

import herokutest
from herokutestapp import views

urlpatterns = [

    path('', views.home),
]