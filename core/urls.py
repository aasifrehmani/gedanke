from django.urls import path
from . import views

urlpatterns =   [
                    path('', views.home, name='homepage'),
                    path('about/', views.about, name='aboutpage'),
                    path('contact/', views.contact, name='contactpage'),
                    path('login/', views.user_login, name='loginpage'),
                    path('logout/', views.user_logoff, name='userlogout'),
                    path('register/', views.register, name='registerpage'),
                ]