from django.urls import path
from . import views

urlpatterns =    [
                    path('', views.index, name='bloghome'),                    
                    path('post/', views.list_single_post, name='blogsinglepost')
                ]