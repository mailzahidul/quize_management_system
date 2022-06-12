from django import forms
from .models import *

class Quizform(forms.ModelForm):
    class Meta:
        model=Quiz
        fields="__all__"