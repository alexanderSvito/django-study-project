from django.http import HttpResponse
from django.shortcuts import render

from shop.models import Car


def list_cars(request, id=None):
    car = Car.objects.get(pk=id)
    return HttpResponse("<li>{}</li><span>{}</span>".format(car.name, car.description))
