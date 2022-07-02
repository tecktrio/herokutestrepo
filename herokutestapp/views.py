from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from herokutestapp.models import ProductList


def home(request):
    return render(request,'index.html')


def register(request):
        #


            return render(request,'register.html')

def registerd(request):

    username = request.POST['user']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username,email,password)
    user.save()
    return HttpResponse("user saved")