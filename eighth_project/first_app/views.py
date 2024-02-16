from django.shortcuts import render, redirect
from .forms import RegisterForm,changUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Create Successfully')
                # messages.warning(request,'warning Create Successfully')
                form.save()
                print(form.cleaned_data)
                # return redirect('login_page')
        else:
            form = RegisterForm()
        return render(request, 'signup.html',{'form':form})
    else:
        return redirect('profile')

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request= request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                passwrd = form.cleaned_data['password']

                user = authenticate(username = name, password = passwrd) 
                if user is not None:
                    login(request, user)
                    return redirect('profile')
                # else:
                #     messages.warning(request,'Incorrect Username or Password')

        else:
            form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})
    else:
        return redirect('profile')

def profile(request):
    if  request.user.is_authenticated:
        if request.method =='POST':
            form = changUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request,'Account Update Successfully')
                # messages.warning(request,'warning Create Successfully')
                form.save()
                # print(form.cleaned_data)
                # return redirect('login_page')
        else:
            form = changUserData(instance = request.user)
        return render(request, 'profile.html',{'form':form})
    else:
        return redirect('signup_page')

def user_logout(request):
    logout(request)
    return redirect('login_page')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login_page')

def pass_change2(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    
    else:
        return redirect('login_page')
    
def user_change_data(request):
    if  request.user.is_authenticated:
        if request.method =='POST':
            form = changUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request,'Account Update Successfully')
                # messages.warning(request,'warning Create Successfully')
                form.save()
                print(form.cleaned_data)
                # return redirect('login_page')
        else:
            form = changUserData()
        return render(request, 'profile.html',{'form':form})
    else:
        return redirect('signup_page')