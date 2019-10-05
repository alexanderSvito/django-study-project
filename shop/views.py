from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from shop.models import Car, CarItem


def cart(request):
    return render(request, 'cart.html')


def welcome(request):
    cars = Car.objects.all()[:7]
    for idx, car in enumerate(cars):
        car.doubled = idx % 6 == 0
    return render(request, "main.html", context={
        "cars": cars,
    })


@require_GET
def search(request):
    q = request.GET.get("q")
    page_num = request.GET.get("page", 1)
    cars = Car.objects.filter(name__contains=q)
    paginator = Paginator(
        cars,
        settings.PER_PAGE,
        orphans=6
    )
    page = paginator.page(page_num)
    return render(request, "search.html", context={
        "page": page,
        "q": q
    })


def list_cars(request, id=None):
    car = Car.objects.get(pk=id)
    return render(request, "detail.html", context={
        "car": car,
    })


@require_POST
def purchase(request, car_id):
    cart = request.cart
    car = get_object_or_404(Car, pk=car_id)
    cart.append(car)
    return redirect("shopping-cart")

@require_POST
def remove_from_cart(request, cart_item_id):
    car_item = get_object_or_404(CarItem, pk=cart_item_id)
    car_item.delete()
    return redirect("shopping-cart")


