# Generated by Django 2.2.5 on 2019-09-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='ffffff', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='engine_volume',
            field=models.PositiveIntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('gus', 'Gus'), ('electr', 'Electricity')], default='petrol', max_length=6),
            preserve_default=False,
        ),
    ]
