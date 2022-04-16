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
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

@login_required
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    id_list = car.options.all().values_list('id')
    options_car_doesnt_have = Option.objects.exclude(id__in=id_list)
    maintenance_form = MaintenanceForm()
    return render(request, 'cars/detail.html', {'car': car, 'maintenance_form': maintenance_form, 'options': options_car_doesnt_have})

@login_required
def add_maintenance(request, car_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.car_id = car_id
        new_maintenance.save()
    return redirect('detail', car_id=car_id)

@login_required
def assoc_option(request, car_id, option_id):
    Car.objects.get(id=car_id).options.add(option_id)
    return redirect('detail', car_id=car_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['year', 'make', 'model', 'color', 'mileage', 'fuel']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['color', 'mileage']


class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'


class OptionList(LoginRequiredMixin, ListView):
    model = Option


class OptionDetail(LoginRequiredMixin, DetailView):
    model = Option


class OptionCreate(LoginRequiredMixin, CreateView):
    model = Option
    fields = '__all__'


class OptionUpdate(LoginRequiredMixin, UpdateView):
    model = Option
    fields = '__all__'


class OptionDelete(LoginRequiredMixin, DeleteView):
    model = Option
    success_url = '/options/'
