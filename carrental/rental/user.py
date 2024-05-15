from django.shortcuts import render
from django.http import HttpResponse

from . import models

def login(request):
     return render(request, 'login.html.jinja')

def logout(request):
    return render(request, 'logout.html.jinja')

def register(request):

    form = models.RegistrationForm()
    return render(request, 'register.html.jinja', {'form': form})