from django.shortcuts import render
from .import forms
from .import models
# Create your views here.
def home(request):
    std = models.Student.objects.all()
    return render(request, 'home.html', {'data':std})

def conact_form(request):
    form = forms.contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'form.html', {'form':form})