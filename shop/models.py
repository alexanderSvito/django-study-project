from django.contrib.sessions.models import Session

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
    active = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User,
        null=True,
        related_name='carts',
        on_delete=models.SET_NULL
    )
    session = models.OneToOneField(
        Session,
        null=True,
        related_name='carts',
        on_delete=models.CASCADE
    )

    @property
    def items_count(self):
        return self.items.count()

    @property
    def has_items(self):
        return self.items.exists()

    @property
    def price(self):
        return self.items.aggregate(
            total=models.Sum('price')
        )['total']

    def append(self, car):
        car_item = CarItem.objects.create(
            name=car.name,
            price=car.price,
            cart=self
        )
        self.items.add(car_item)


class AbstractCar(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

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
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
