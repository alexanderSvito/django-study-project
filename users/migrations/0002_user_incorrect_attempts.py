# Generated by Django 2.2.5 on 2019-09-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='incorrect_attempts',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
