from django.shortcuts import render
from django.http import HttpResponse

def dashboard_home(request):
    return render(request, 'dashboard_home.html')

def dashboard_stats(request):
    return render(request, 'dashboard_stats.html')