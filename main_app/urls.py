from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('cars/', views.cars_index, name="index"),
	path('cars/<int:car_id>/', views.cars_detail, name="detail"),
	path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
	path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
	path('cars/<int:car_id>/add_maintenance', views.add_maintenance, name='add_maintenance'),
	path('options/', views.OptionList.as_view(), name='options_index'),
	path('options/<int:pk>/', views.OptionDetail.as_view(), name='options_detail'),
	path('options/create/', views.OptionCreate.as_view(), name='options_create'),
	path('options/<int:pk>/update/', views.OptionUpdate.as_view(), name='options_update'),
	path('options/<int:pk>/delete/', views.OptionDelete.as_view(), name='options_delete'),
	path('cars/<int:car_id>/assoc_option/<int:option_id>', views.assoc_option, name='assoc_option'),
	path('accounts/signup/', views.signup, name='signup'),
]