from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def cars_index(request):
	return render(request, 'cars/index.html') #{ 'cars': cars })