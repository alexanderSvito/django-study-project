# Generated by Django 2.2.5 on 2019-09-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190928_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='initial_secret_key',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]