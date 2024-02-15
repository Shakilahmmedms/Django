from django.shortcuts import render
from album.models import Album

def home(request):
    alb_data = Album.objects.all()
    # print(ms_data)
    # print(alb_data)
 
    return render(request,'home.html',{'data':alb_data})