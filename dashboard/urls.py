from django.urls import path
from . import views

urlpatterns =   [
                    path('', views.dashboard_home, name='dashboardhome'),
                    path('stats/', views.dashboard_stats, name='dashboardstats'),
                ]