from django import forms
from .models import matches,analysis

class MatchesForm(forms.ModelForm):
    class Meta:
        model = matches
        fields = ['date', 'place','isplayed']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'place': forms.TextInput(attrs={'maxlength': 10}),
        }


class analysisform(forms.ModelForm):
    class Meta:
        model = analysis
        fields = ['desc', 'pic', 'video']