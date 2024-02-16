from django.shortcuts import render,redirect
from Task.forms import TaskForm
from .import models
from .import forms
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    else:
        task_form = TaskForm()
    return render(request, 'add_task.html' ,{'form':task_form})

def edit_task(request, id):
    task = models.Task.objects.get(pk = id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    return render(request, 'add_task.html' ,{'form':task_form})

def delete_task(request, id):
    task = models.Task.objects.get(pk = id)
    task.delete()
    return redirect('show_task')