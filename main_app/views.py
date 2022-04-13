import imp
from operator import mod
from django.shortcuts import redirect, render

from main_app.forms import MaintenanceForm
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
	maintenance_form = MaintenanceForm()
	return render(request, 'cars/detail.html', { 'car': car, 'maintenance_form': maintenance_form })

def add_maintenance(request, car_id):
	form = MaintenanceForm(request.POST)
	if form.is_valid():
		new_maintenance = form.save(commit=False)
		new_maintenance.car_id = car_id
		new_maintenance.save()
	return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
	model = Car
	fields = '__all__'

class CarUpdate(UpdateView):
	model = Car
	fields = ['color', 'mileage']

class CarDelete(DeleteView):
	model = Car
	success_url = '/cars/'
