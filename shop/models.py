from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField()

    class Meta:
        pass

    def __str__(self):
        return self.name
