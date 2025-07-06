from django.shortcuts import render

def index(request):
    return render(request, 'blog_home.html')

def list_single_post(request):
    return render(request, 'single_post.html')