from django.shortcuts import render
from . import models


# Create your views here.
def cars_view(request):
    if request.method == 'GET':
        cars = models.Cars.objects.all()
        return render(request, 'cars.html', {'cars': cars})

