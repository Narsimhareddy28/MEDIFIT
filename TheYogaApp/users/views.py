from datetime import date

from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserRegistrationForm, LoginForm, UserProfileForm
from .models import Profile

User = get_user_model()


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"Hi! {username}")
                return HttpResponseRedirect('/dashboard/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "HE username or password.")
    form = LoginForm()
    return render(request, "login.html", {"form": form})


        
    

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['emailId'],
                password=make_password(form.cleaned_data['password']),
            )
            profile = Profile.objects.create(
                user=user,
                f_name=form.cleaned_data['f_name'],
                l_name=form.cleaned_data['l_name'],
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight'],
                dob=form.cleaned_data['dob'],
                gender=form.cleaned_data['gender'],
                exercise_frequency=form.cleaned_data['exercise_frequency']
            )
            profile.medical_conditions.set(form.cleaned_data['medical_conditions'])
            profile.diet.set(form.cleaned_data['diet'])
            messages.success(request, "Account is created. You can now login to the account.")
            return HttpResponseRedirect('/users/login/')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/users/login/')
