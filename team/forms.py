from django import forms
from .models import teams


class teamform(forms.ModelForm):
    class Meta:
        model = teams
        fields = ['title', 'desc','password']

        widgets = {  
            'password': forms.PasswordInput(),  # Use a password input for security  
        }  