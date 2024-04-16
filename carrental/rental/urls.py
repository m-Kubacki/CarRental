<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('car/<car_id>', views.car, name='car'),
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cars/', views.cars, name='cars'),
    # path('car/<car_id>', views.car name='car')
>>>>>>> 8b4e9cc810cff4b284d5d53ac73ed907bdb89d13
]