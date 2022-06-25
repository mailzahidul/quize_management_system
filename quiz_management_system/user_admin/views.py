from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import User
# Create your views here.


def user_registration(request):

    if request.POST:
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        # username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user_check = authenticate(email=email, password=password1)
            if user_check is None:
                try:
                    User.objects.create_staffuser(email=email, password=password1)
                    messages.success(request, "Sign Up Successfully, Login please")
                    return redirect('login')
                except Exception as errors:
                    messages.error(request, f" {errors}")
            else:
                messages.error(request, "Username Already Exist.")
        else:
            messages.warning(request, "Password not match.")
        return render(request, 'user/registration.html')
    return render(request, 'user/registration.html')


def user_login(request):
    if request.POST:
        email = request.POST['email_id']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        try:
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Email or password incorrect.')
        except Exception as err:
            messages.error(request, f'{err}')

    return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')