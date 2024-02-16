from django.shortcuts import render,redirect
from .import views
from Task.models import Task

def show_task(request):
    data = Task.objects.all()
    return render(request, 'show_task.html', {'data':data})