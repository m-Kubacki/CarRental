<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html.jinja')

def index(request):
    return render(request, 'cars.html.jinja')

def index(request, car_id):
    return render(request, 'car.html.jinja' )
=======
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'cars.html')

def index(request, car_id):
    return render(request, 'car.html' )
>>>>>>> 8b4e9cc810cff4b284d5d53ac73ed907bdb89d13
