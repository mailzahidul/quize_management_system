from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User, Group
# Create your views here.


def user_registration(request):
    if request.user.is_authenticated:
        messages.success(request, "You have already an account...")
        return redirect('home')

    if request.POST:
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user_check = authenticate(username=username, password=password1)
            if user_check is None:
                try:
                    User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password1)
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
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'user/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')