from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from .import models
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = forms.SignUpForm(request.POST)
        if signup_form.is_valid():
            messages.success(request,'Account Created Successfuly')
            signup_form.save()
            return redirect('signup')
    else:   
        signup_form = forms.SignUpForm()
    return render(request,'sign_up.html',{'form':signup_form ,'type': 'Sign Up'})

#class base view
#user login class base view
class UserLoginView(LoginView):
    template_name = 'sign_up.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Login Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Incorrect Information')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    


# class EditUserData(LoginView):
#     model = models.