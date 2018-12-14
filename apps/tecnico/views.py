from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.tecnico.forms  import TecnicoForm
from apps.tecnico.models import Tecnico
# Create your views here.

def index(request):
	return render(request, 'formulario/tecnico.html')

def tecnico_view(request):
	if request.method == 'POST':
		form = TecnicoForm(request.POST)
		if form.is_valid():
			form.save()
		
	else:
		form = TecnicoForm()
	return render(request, 'tecnico/tecnico.html',{'form':form})

def tecnico_list(request):
	tecnico = Tecnico.objects.all()
	contexto = {'tecnico':tecnico}
	return render(request, 'tecnico/tecnico_list.html',contexto)