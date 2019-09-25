from django.urls import path

from shop import views


urlpatterns = [
    path("cars/<int:id>", views.list_cars),
    path("search", views.search),
    path("accounts/login/", views.login_view),
    path("logout", views.logout_view),
    path("cart", views.cart),
    path("", views.welcome)
]
