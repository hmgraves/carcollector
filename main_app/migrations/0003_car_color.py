# Generated by Django 4.0.3 on 2022-04-12 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_car_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='color', max_length=100),
        ),
    ]
