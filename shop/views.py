from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.contrib.auth import authenticate, logout, login

from shop.models import Car


def login_view(request):
    if request.method == 'GET':
        return render(request, "login.html", context={
            "error": False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            print(request.GET.get('next'))
            return redirect('/')
        else:
            return render(request, "login.html", context={
                "error": True
            })


@login_required
def cart(request):
    cart = request.user.carts.all()[-1]
    return render(request, 'cart.html', context={
        "cart": cart
    })


def logout_view(request):
    logout(request)
    return redirect("/")

def welcome(request):
    cars = Car.objects.all()[:3]
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