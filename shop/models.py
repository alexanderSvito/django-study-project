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


class Car(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField()
    fuel_type = models.CharField(
        max_length=6,
        choices=FuelType.get_choices()
    )
    engine_volume = models.PositiveIntegerField()
    color = models.CharField(max_length=6)

    class Meta:
        pass

    def __str__(self):
        return self.name
