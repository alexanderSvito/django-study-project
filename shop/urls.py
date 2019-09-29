from django.urls import path

from shop import views


urlpatterns = [
    path("cars/<int:id>", views.list_cars),
    path("search", views.search),
    path("cart", views.cart),
    path("", views.welcome)
]
