import json
import os

from django.core.management import BaseCommand
from django.conf import settings

from shop.models import Car


SEED_FILE = os.path.join(
    settings.BASE_DIR,
    'static',
    'cars.json'
)


class Command(BaseCommand):
    help = 'Populates the database with seed data'

    def add_arguments(self, parser):
        parser.add_argument('--truncate', '-t', default=False, action='store_true')

    def handle(self, *args, **options):
        if options['truncate']:
            Car.objects.all().delete()

        with open(SEED_FILE) as f:
            cars = json.load(f)

        bulk_cars = []
        for car in cars:
            bulk_cars.append(
                Car(
                    name=car['name'],
                    description=car['description'],
                    year=car['year'] + '-01-01',
                    price=car['price'],
                    mileage=car['mileage'],
                    fuel_type=car['fuel'],
                    engine_volume=car['volume'],
                    color=car['color'],
                    picture=car['img']
                )
            )
            self.stdout.write(f"Car {car['name']} processed")

        Car.objects.bulk_create(bulk_cars)