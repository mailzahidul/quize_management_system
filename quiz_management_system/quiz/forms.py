from django import forms
from .models import *

class Quizform(forms.ModelForm):
    class Meta:
        model=Quiz
        fields="__all__"
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'option_1': forms.TextInput(attrs={'class': 'form-control'}),
            'option_2': forms.TextInput(attrs={'class': 'form-control'}),
            'option_3': forms.TextInput(attrs={'class': 'form-control'}),
            'option_4': forms.TextInput(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'answer': forms.TextInput(attrs={'class': 'form-control'})
        }
