import json

from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import ReadingGuide
from .forms import ListForm

# Create your views here.
def home(request):
    '''Render the homepage of the website'''

    # Deal with login function on home page
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('comic_list.html')
    else:
        form = AuthenticationForm()
    return render(request, 'pages/home.html', {'form': form})


def register(request):
    '''Function to register new users to the site'''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Return user back to home page to login
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def guide_view(request): 
    '''Function to display comic lists associated with the user'''
    lists = ReadingGuide.objects.filter(creator=request.user)
    return render(request, 'pages/guide_view.html', {'lists': lists})


def create_list(request):
    '''Function to allow users to create a comic list'''
    form = ListForm()
    return render(request, 'pages/create_list.html', {'form': form})
