from django.shortcuts import render, redirect
from post.models import Posts

def  home(request):
    data = Posts.objects.all()
    # print(data)
    return render(request, 'home.html',{'data':data})