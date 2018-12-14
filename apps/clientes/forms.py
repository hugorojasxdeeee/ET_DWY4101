from django import forms

from apps.clientes.models import Cliente


class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = [
			'idc',
			'nombre',
			'direccion',
			'ciudad',
			'comuna',
			'telefono',
			'email',
		]
		labels = {
			'idc': 'ID cliente',
			'nombre': 'Nombre',
			'direccion': 'Direccion',
			'ciudad':'Ciudad',
			'comuna': 'Comuna',
			'telefono': 'Telefono',
			'email': 'Correo',
		}
		widgets = {
			'idc': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'ciudad': forms.TextInput(attrs={'class':'form-control'}),
			'comuna': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
		}