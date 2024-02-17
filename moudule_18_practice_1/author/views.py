from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = forms.SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request,'Account Create Successfully')
            return redirect('signup')
    else:
        signup_form = forms.SignUpForm()
    return render(request,'sign_up.html',{'form':signup_form, 'type':'SignUp'})

# @login_required
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.success(request, 'Login Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Incorrect Login Information')
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'sign_up.html', {'form':form, 'type':'Login'})

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = forms.changeUserData(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile update Successfully')
            return redirect('profile')
    else:
        profile_form = forms.changeUserData(instance = request.user)
    return render(request, 'profile.html', {'form': profile_form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Log Out Successfully')
    return redirect('login')

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user , data = request.POST)
        if form.is_valid():
            messages.success(request, 'Password update Successfully')
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form': form})

@login_required
def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user , data = request.POST)
        if form.is_valid():
            messages.success(request, 'Password update Successfully')
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'pass_change.html', {'form': form})

