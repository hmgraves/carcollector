from operator import mod
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPES = (
	('B', 'Brakes'),
	('O', 'Oil change'),
	('T', 'Tires'),
	('W', 'Windshield wipers')
)

class Option(models.Model):
	options = models.CharField(max_length=100)

	def __str__(self):
		return self.options
	
	def get_absolute_url(self):
		return reverse('options_detail', kwargs={'pk': self.id})


class Car(models.Model):
	year = models.IntegerField()
	make = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	color = models.CharField(max_length=100, default='')
	mileage = models.IntegerField()
	fuel = models.CharField(max_length=100, default='')
	options = models.ManyToManyField(Option)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.model

	def get_absolute_url(self):
		return reverse('detail', kwargs={'car_id': self.id})

class Maintenance(models.Model):
	date = models.DateField()
	type = models.CharField(
		max_length=1,
		choices=TYPES,
		default=TYPES[0][0]
	)

	car = models.ForeignKey(Car, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.get_type_display()} on {self.date}"