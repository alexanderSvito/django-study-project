from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

from shop.models import Car



@login_required
def cart(request):
    cart = request.user.carts.all()[0]
    return render(request, 'cart.html', context={
        "cart": cart
    })


def welcome(request):
    cars = Car.objects.all()[:7]
    for idx, car in enumerate(cars):
        car.doubled = idx % 6 == 0
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
