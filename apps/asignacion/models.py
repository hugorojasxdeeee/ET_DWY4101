from django.db import models
from apps.clientes.models import Cliente
from apps.tecnico.models import Tecnico

# Create your models here.


class Asignacion(models.Model):
	folio = models.CharField(max_length=10, primary_key=True)
	ncliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
	ntecnico = models.ForeignKey(Tecnico, null=True, blank=True, on_delete=models.CASCADE)
