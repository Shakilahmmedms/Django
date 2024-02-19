from django.shortcuts import render,redirect
from car_post.models import CarPosts
def home(request):
    data = CarPosts.objects.all()
    return render(request,'home.html' ,{'data':data})