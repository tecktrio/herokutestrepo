from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import message
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from herokutestapp.models import ProductList


def home(request):
    return render(request,'index.html')


def register(request):
            return render(request,'register.html')

def registerd(request):

    username = request.POST['user']
    email = request.POST['email']
    password = request.POST['password']

    user = auth.authenticate(username=username,password=password)
    if user is not None:

        return render(request,'index.html')
    else:
        return HttpResponse("please try again")
    # if User.objects.filter(username=username).exists():
    #     return HttpResponse("the username is already taken")
    # else:
    #
    #     user = User.objects.create_user(username,email,password)
    #     user.save()
    #     return HttpResponse("user registerd")