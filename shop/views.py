from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from shop.models import Car


def welcome(request):
    cars = Car.objects.all()
    return render(request, "main.html", context={
        "cars": cars
    })


@require_GET
def search(request):
    q = request.GET.get("q")
    cars = Car.objects.filter(name__contains=q)
    return render(request, "main.html", context={
        "cars": cars
    })


def list_cars(request, id=None):
    car = Car.objects.get(pk=id)
    return render(request, "detail.html", context={
        "car": car
    })