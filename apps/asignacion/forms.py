from django import forms

from apps.asignacion.models import Asignacion


class AsignacionForm(forms.ModelForm):

	class Meta:
		model = Asignacion

		fields = [
			'folio',
			'ncliente',
			'ntecnico',
			
		]
		labels = {
			'folio': 'Folio de asignacion',
			'ncliente': 'Cliente',
			'ntecnico': 'Tecnico',
		}
		widgets = {
			'folio': forms.TextInput(attrs={'class':'form-control'}),
			'ncliente': forms.Select(attrs={'class':'form-control'}),
			'ntecnico': forms.Select(attrs={'class':'form-control'}),