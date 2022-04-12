import imp
from operator import mod
from django.shortcuts import render
from .models import Car
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def cars_index(request):
	cars = Car.objects.all()
	return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	return render(request, 'cars/detail.html', { 'car': car })

class CarCreate(CreateView):
	model = Car
	fields = '__all__'

class CarUpdate(UpdateView):
	model = Car
	fields = ['color', 'mileage']

class CarDelete(DeleteView):
	model = Car
	success_url = '/cars/'
