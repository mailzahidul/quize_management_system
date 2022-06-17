from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"

class CreateUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"