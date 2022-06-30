from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


USER_TYPE= [
    ('student', 'Student'),
    ('teacher', 'Teacher')
    ]


class createuserform(forms.ModelForm):
    user_type= forms.CharField(widget=forms.Select(choices=USER_TYPE))
    class Meta:
        model = User
        fields = ('f_name', 'l_name', 'user_type','email', 'password')
        widgets = {
            'f_name' : forms.TextInput(attrs={'class':'form-control'}),
            'l_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'type':'email', 'autocomplete':'off'}),
            'password' : forms.TextInput(attrs={'class':'form-control', 'type':'password'}),
        }


class Permissionform(forms.ModelForm):
    user_type= forms.CharField(widget=forms.Select(choices=USER_TYPE))
    class Meta:
        model = User
        fields = ('user_type','active')
        widgets = {
            'f_name' : forms.TextInput(attrs={'class':'form-control'}),
            'l_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'type':'email', 'autocomplete':'off'})
        }