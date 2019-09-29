from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from users.forms import RegistrationForm
from users.models import User


def logout_view(request):
    logout(request)
    return redirect("/")

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
            return redirect('/')
        else:
            try:
                user = User.objects.get(username=username)
                user.incorrect_attempts += 1
                if user.incorrect_attempts > settings.INCORRECT_ATTEMPTS_LIMIT:
                    user.is_active = False
                user.save()
            except User.DoesNotExist:
                pass
            return render(request, "login.html", context={
                "error": True
            })

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(
            request.POST
        )
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.verify_email()
            redirect("/")
    else:
        form = RegistrationForm()
    return render(request, "register.html", context={
        "form": form
    })

@require_GET
def verify_email(request):
    key = request.GET.get("key")
    if request.user.check_key(key):
        request.user.is_email_verified = True
        request.user.save()
    redirect("/")