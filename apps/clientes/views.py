from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.clientes.forms import ClienteForm
from apps.clientes.models import Cliente
# Create your views here.

def index(request):
    return render(request, 'index/index.html')
    
def formulario_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = ClienteForm()
    
    return render(request, 'cliente/cliente.html',{'form':form})

def cliente_list(request):
	cliente = Cliente.objects.all()
	contexto = {'cliente':cliente}
	return render(request, 'cliente/cliente_list.html',contexto)