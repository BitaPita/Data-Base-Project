from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse


def SignupView (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
      
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)  #user will automatically be loged in after signing up
            return HttpResponse('user has been created!')

    form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


def LoginView (request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse('You are in')

    form = AuthenticationForm()
    return render (request, 'account/login.html', {'form': form})




