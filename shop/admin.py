from django.contrib import admin
from shop.models import Car, CarItem, Cart

admin.site.register(Car)
admin.site.register(Cart)
admin.site.register(CarItem)

