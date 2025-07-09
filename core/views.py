from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_logoff(request):
    user_logout(request)
    messages.success(request, "User logout successfully!")
    return redirect('loginpage')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"User loggedin successfully!")
            return redirect('user_dashboard')
        else:            
            messages.error(request, f"Erro! Invalid username or password.")
            return redirect('loginpage')
    else:
        return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')