# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User,playerProfile,coachProfile


class playerSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.base_role = User.Role.PLAYER
        if commit:
              user.save()
              # playerProfile.objects.create(user=user)
        return user


class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = playerProfile
        fields = ['pos', 'age', 'number','pic', 'first_name', 'last_name']

class coachSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.base_role = User.Role.COACH
        if commit:
            user.save()
            # coachProfile.objects.create(user=user)
        return user



class LoginForm(AuthenticationForm):
    pass