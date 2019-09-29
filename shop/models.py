from users.models import User
from django.db import models
from enum import Enum


class FuelType(Enum):
    Petrol = 'petrol'
    Diesel = 'diesel'
    Gus = 'gus'
    Electricity = 'electr'

    @classmethod
    def get_choices(cls):
        return [
            (el.value, name)
            for name, el in cls.__members__.items()
        ]


class Cart(models.Model):
    created = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User,
        null=True,
        related_name='carts',
        on_delete=models.SET_NULL
    )

    @property
    def price(self):
        return self.items.all().values_list('price')


class AbstractCar(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True


class CarItem(AbstractCar):
    cart = models.ForeignKey(
        Cart,
        related_name='items',
        on_delete=models.CASCADE
    )


class Car(AbstractCar):
    description = models.TextField()
    year = models.DateField()
    mileage = models.PositiveIntegerField()
    fuel_type = models.CharField(
        max_length=6,
        choices=FuelType.get_choices()
    )
    engine_volume = models.PositiveIntegerField()
    color = models.CharField(max_length=6)
    picture = models.ImageField(null=True, upload_to='img/')

    class Meta:
        pass

    def __str__(self):
        return self.name
