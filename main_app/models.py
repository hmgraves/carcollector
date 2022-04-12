from django.urls import reverse
from django.db import models

# Create your models here.

class Car(models.Model):
	year = models.IntegerField()
	make = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	color = models.CharField(max_length=100, default='')
	mileage = models.IntegerField()

	def __str__(self):
		return self.model

	def get_absolute_url(self):
		return reverse('detail', kwargs={'car_id': self.id})	