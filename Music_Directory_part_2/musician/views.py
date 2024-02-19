from django.shortcuts import render,redirect
from .import forms
from django.views.generic import CreateView
from .import models
from django.urls import reverse_lazy
# Create your views here.

def create_musician(request):
    if request.method =='POST':
        musican_form = forms.MusicianForm(request.POST)
        if musican_form.is_valid():
            musican_form.save()
            return redirect('create_musician')
        
    else:
        musican_form = forms.MusicianForm()
    return render(request, 'create_musician.html' ,{'form': musican_form})

class CreatMusicianView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'create_musician.html'
    success_url = reverse_lazy('create_musician')
