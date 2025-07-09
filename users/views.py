from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def user_home(request):
    return render(request, 'user_dashboard.html')

@login_required()
def user_index(request):
    return render(request, 'user_dashboard.html')


def user_register(request):
    if request.method == "POST":
        users = User.objects.all()
        frm_register = UserRegistrationForm(request.POST)

        if frm_register.is_valid():
            user = frm_register.save()
            print("User created successfully.")
            messages.success(request, f'Account created for {user.username}!')
            return redirect('loginpage')  # Redirect to login after success
        else:
            # Pass form with errors back to template
            messages.error(request, 'Please correct the errors below.')
        
    else:
        users = User.objects.all()
        frm_register = UserRegistrationForm()

    return render(request, 'register.html', context={'frm_register':frm_register, 'users': users})