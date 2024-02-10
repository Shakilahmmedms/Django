from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse('This is app/Courses Page')

def about(request):
    return HttpResponse('This is app/ About Page')

def home(request):
    return HttpResponse('This is app/ Home Page')
