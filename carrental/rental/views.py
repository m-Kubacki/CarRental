from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html.jinja')

def index(request):
    return render(request, 'cars.html.jinja')

def index(request):
    return render(request, 'car.html.jinja' )
