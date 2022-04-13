from django.forms import ModelForm
from .models import Maintenance

class MaintenanceForm(ModelForm):
	class Meta:
		model = Maintenance
		fields = ['date', 'type']