from django.shortcuts import render, redirect
from .import form
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Posts

# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form = form.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:   
#         author_form = form.AuthorForm()
#     return render(request,'add_author.html',{'form':author_form})

def register(request):
    if request.method == 'POST':
        register_form = form.RegistrationForm(request.POST)
        if register_form.is_valid():
            messages.success(request,'Account Created Successfuly')
            register_form.save()
            return redirect('register')
    else:   
        register_form = form.RegistrationForm()
    return render(request,'register.html',{'form':register_form ,'type': 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password= user_pass)
            if user is not None:
                messages.success(request,'LogIn Successfuly')
                login(request , user)
                return redirect('profile')
            else:
                messages.warning(request,'Login Information Incorrect')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html' ,{'form' : form, 'type': 'Login'})

@login_required
def profile(request):
    data = Posts.objects.filter(author = request.user)
    return render(request,'profile.html',{'data':data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = form.changUserData(request.POST, instance = request.user)
        if profile_form.is_valid():
            messages.success(request,'Profile Updated Successfuly')

            profile_form.save()
            return redirect('profile')
    else:   
        profile_form = form.changUserData(instance = request.user)
    return render(request,'update_profile.html',{'form':profile_form })

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            messages.success(request,'Password Updated Successfuly')
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:   
        form = PasswordChangeForm(request.user)
    return render(request,'pass_change.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')