from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views import View
from .forms import playerSignUpForm, coachSignUpForm,LoginForm
from .models import User


class playerSignUpView(View):
    def get(self, request):
        form = playerSignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = playerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, 'Student registration successful!')
            return redirect('login')  # Change to your desired redirect page
        messages.error(request, 'Registration failed. Please check your data.')
        return render(request, 'signup.html', {'form': form})

class coachSignUpView(View):
    def get(self, request):
        form = coachSignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = coachSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, 'Teacher registration successful!')
            return redirect('login')  # Change to your desired redirect page
        messages.error(request, 'Registration failed. Please check your data.')
        return render(request, 'signup.html', {'form': form})

class SignupView(View):
    def get(self, request):
        form1 = coachSignUpForm()
        form2 = playerSignUpForm()
        return render(request, 'signup.html', {'form1': form1,'form2':form2})

    def post(self, request):
        form1 = coachSignUpForm(request.POST)
        form2 = playerSignUpForm(request.POST)
        if form1.is_valid():
            user = form1.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, 'coach registration successful!')
            return redirect('login')  # Change to your desired redirect page
        if form2.is_valid():
            user = form2.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, 'player registration successful!')
            return redirect('login')  # Change to your desired redirect page
        messages.error(request, 'Registration failed. Please check your data.')
        return render(request, 'signup.html', {'form1': form1,'form2':form2})

def signupview(request):
    form1 = coachSignUpForm(request.POST)
    form2 = playerSignUpForm(request.POST)
    if request.method == "POST":
        if 'submit1' in request.POST:
            form1 = coachSignUpForm(request.POST)
            if form1.is_valid():
                user = form1.save()
                login(request, user)  # Auto-login after registration
                messages.success(request, 'coach registration successful!')
                return redirect('login')  # Change to your desired redirect page
        elif 'submit2' in request.POST:
            form2 = playerSignUpForm(request.POST)
            if form2.is_valid():
                user = form2.save()
                login(request, user)  # Auto-login after registration
                messages.success(request, 'player registration successful!')
                return redirect('login')  # Change to your desired redirect page
    return render(request, 'signup.html', {'form1': form1, 'form2': form2})
def sview(request):
    return render(request, 'home.html',)

def cview(request):
    return render(request, 'check.html',)
def vview(request):
    return render(request, 'signup.html',)

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            #ins=User.objects.get_by_natural_key(user.username)
            if user is not None and user.role == User.Role.PLAYER:
                return redirect('check')
            elif user is not None and user.role == User.Role.COACH:
                return redirect('home')
            elif user is not None and user.role == User.Role.ADMIN:
                return redirect('player_signup')
        return render(request, 'login.html', {'form': form})