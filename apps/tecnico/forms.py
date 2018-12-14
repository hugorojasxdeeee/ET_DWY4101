from django import forms

from apps.tecnico.models import Tecnico


class TecnicoForm(forms.ModelForm):

	class Meta:
		model = Tecnico

		fields = [
			'idt',
			'email',
			'contraseña',
			
		]
		labels = {
			'idt': 'ID tecnico',
			'email': 'Correo',
			'contraseña': 'Contraseña',
		}
		widgets = {
			'idt': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'contraseña': forms.TextInput(attrs={'class':'form-control'}),
		}