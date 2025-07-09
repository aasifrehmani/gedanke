from django.urls import path
from . import views

urlpatterns =   [
                    path('', views.user_index, name='user_dashboard'),
                    path('profile/', views.user_home, name='user_profile'),
                    path('register/', views.user_register, name='user_register'),
                ]