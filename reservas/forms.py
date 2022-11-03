from django import forms
from .models import Reserva
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

# Create your forms here.

class NuevaReserva(forms.ModelForm):
	class Meta:
		model = Reserva
		fields = [ 'fecha_hora_desde','fecha_hora_hasta']
		widgets = {
			'fecha_hora_desde': DateTimePickerInput(),
			'fecha_hora_hasta': DateTimePickerInput(),

			}
