from django.shortcuts import render, redirect
from .import forms
from .import models
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView,DeleteView
# Create your views here.
def creat_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('create_album')
    else:
        album_form = forms.AlbumForm()
    return render(request,'create_album.html' , {'form':album_form})

#class base view
class CreateAlbumView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'create_album.html'
    success_url =reverse_lazy('create_album')
    def form_valid(self, form):
        return super().form_valid(form)
    


def edit_album(request, id):
    album = models.Album.objects.get(pk = id)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request,'create_album.html' , {'form':album_form})

# class base view

class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    pk_url_kwarg = 'id'
    template_name = 'create_album.html'
    success_url = reverse_lazy('homepage')
    


def delete_album(request,id):
     album = models.Album.objects.get(pk = id)
     album.delete()
     return redirect('homepage')

class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'