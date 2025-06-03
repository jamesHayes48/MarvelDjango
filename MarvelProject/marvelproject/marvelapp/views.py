import json

from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

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


