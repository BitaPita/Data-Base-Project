from django import forms
from .models import teams,drill,Strat,diet


class teamform(forms.ModelForm):
    class Meta:
        model = teams
        fields = ['title', 'desc','password','pic']

        widgets = {
            'password': forms.PasswordInput(),  # Use a password input for security
        }

class drillform(forms.ModelForm):
    class Meta:
        model = drill
        fields = ['title', 'desc', 'video']

class stratform(forms.ModelForm):
    class Meta:
        model = Strat
        fields = ['title', 'desc']


class dietform(forms.ModelForm):
    class Meta:
        model = diet
        fields = ['title', 'desc','meal','day']
