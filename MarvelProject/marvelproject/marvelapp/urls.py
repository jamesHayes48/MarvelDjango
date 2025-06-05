from django.urls import path, include 
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('guide_view/', views.guide_view, name='guide_view'),
]
