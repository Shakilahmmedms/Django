from django.shortcuts import render,redirect
from .import views

def home(request):
    return render(request,'home.html')