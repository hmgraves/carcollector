from dataclasses import field, fields
import imp
from lib2to3.pgen2.token import OP
from operator import mod
from pyexpat import model
from django.shortcuts import redirect, render

from main_app.forms import MaintenanceForm
from .models import Car, Option
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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
	id_list = car.options.all().values_list('id')
	options_car_doesnt_have = Option.objects.exclude(id__in=id_list)
	maintenance_form = MaintenanceForm()
	return render(request, 'cars/detail.html', { 'car': car, 'maintenance_form': maintenance_form, 'options': options_car_doesnt_have })

def add_maintenance(request, car_id):
	form = MaintenanceForm(request.POST)
	if form.is_valid():
		new_maintenance = form.save(commit=False)
		new_maintenance.car_id = car_id
		new_maintenance.save()
	return redirect('detail', car_id=car_id)

def assoc_option(request, car_id, option_id):
	Car.objects.get(id=car_id).options.add(option_id)
	return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
	model = Car
	fields = ['year', 'make', 'model', 'color', 'mileage', 'fuel']

class CarUpdate(UpdateView):
	model = Car
	fields = ['color', 'mileage']

class CarDelete(DeleteView):
	model = Car
	success_url = '/cars/'

class OptionList(ListView):
	model = Option

class OptionDetail(DetailView):
	model = Option

class OptionCreate(CreateView):
	model = Option
	fields = '__all__'

class OptionUpdate(UpdateView):
	model = Option
	fields = '__all__'

class OptionDelete(DeleteView):
	model = Option
	success_url = '/options/'