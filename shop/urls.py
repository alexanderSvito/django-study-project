from django.urls import path

from shop import views


urlpatterns = [
    path("cars/<int:id>", views.list_cars),
    path(
        "purchase/<int:car_id>",
        views.purchase,
        name='purchase-car'
    ),
    path(
        "remove/<int:cart_item_id>",
        views.remove_from_cart,
        name='remove-car-from-cart'
    ),
    path("search", views.search),
    path("cart", views.cart, name='shopping-cart'),
    path("", views.welcome)
]
