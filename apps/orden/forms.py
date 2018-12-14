from django import forms

from apps.orden.models import Orden


class OrdenForm(forms.ModelForm):

	class Meta:
		model = Orden

		fields = [
			'cliente',
			'tecnico',
			'fecha',
			'hora_inicio',
			'hora_termino',
			'idascensor',
			'fallas',
			'reparacion',
			'piezas',
			'nombreReceptor',
			
		]
		labels = {
			'cliente': 'Cliente',
			'tecnico': 'Tecnico',
			'fecha': 'Fecha',
			'hora_inicio': 'Hora inicio',
			'hora_termino': 'Hora termino',
			'idascensor': 'ID ascensor',
			'fallas': 'Fallas',
			'reparacion': 'Reparacion',
			'piezas': 'Piezas',
			'nombreReceptor': 'Nombre Receptor',
		}
		widgets = {
			'cliente': forms.Select(attrs={'class':'form-control'}),
			'tecnico': forms.Select(attrs={'class':'form-control'}),
			'fecha': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'hora_inicio': forms.TextInput(attrs={'class':'form-control','type':'time'}),
			'hora_termino': forms.TextInput(attrs={'class':'form-control','type':'time'}),
			'idascensor': forms.TextInput(attrs={'class':'form-control'}),
			'fallas': forms.TextInput(attrs={'class':'form-control'}),
			'reparacion': forms.TextInput(attrs={'class':'form-control'}),
			'piezas': forms.TextInput(attrs={'class':'form-control'}),
			'nombreReceptor': forms.TextInput(attrs={'class':'form-control'}),
			}

