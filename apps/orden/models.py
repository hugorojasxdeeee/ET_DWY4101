from django.db import models
from apps.clientes.models import Cliente
from apps.tecnico.models import Tecnico


# Create your models here.

class Orden(models.Model):
	cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
	tecnico = models.ForeignKey(Tecnico, null=True, blank=True, on_delete=models.CASCADE)
	fecha = models.DateField()
	hora_inicio = models.TimeField()
	hora_termino = models.TimeField()
	idascensor = models.CharField(max_length=10)
	fallas = models.TextField()
	reparacion = models.TextField()
	piezas = models.CharField(max_length=50)
	nombreReceptor = models.CharField(max_length=50)