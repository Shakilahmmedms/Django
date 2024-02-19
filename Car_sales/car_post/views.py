from django.shortcuts import render,redirect
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView,DetailView
from django.utils.decorators import method_decorator

# class AddCarView(CreateView):
#     model = 

# @method_decorator(login_required, name='dispatch')
# class AddCarView(CreateView):
#     model = models.CarPosts
#     form_class = forms.CarForm
#     template_name = 'home.html'
#     success_url = reverse_lazy('add_car')
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

def Car_list(request):
    data = models.CarPosts.objects.all()
    return render(request,'home.html', {'data':data})
