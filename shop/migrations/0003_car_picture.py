# Generated by Django 2.2.5 on 2019-09-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190918_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
