from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.orden.forms  import OrdenForm
from apps.orden.models import Orden

# Create your views here.

def index(request):
	return render(request, 'formulario/orden.html')

def orden_view(request):
	if request.method == 'POST':
		form = OrdenForm(request.POST)
		if form.is_valid():
			form.save()
		
	else:
		form = OrdenForm()
	return render(request, 'orden/orden.html', {'form':form})

def orden_list(request):
	orden = Orden.objects.all()
	contexto = {'orden':orden}
	return render(request, 'orden/orden_list.html',contexto)