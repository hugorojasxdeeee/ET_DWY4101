from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.asignacion.forms  import AsignacionForm
from apps.asignacion.models import Asignacion

# Create your views here.

def index(request):
	return render(request, 'asignacion/asignacion.html')

def asignacion_view(request):
	if request.method == 'POST':
		form = AsignacionForm(request.POST)
		if form.is_valid():
			form.save()
		
	else:
		form = AsignacionForm()
	return render(request, 'asignacion/asignacion.html', {'form':form})

