from django.db import models

# Create your models here.


class Cliente(models.Model):
	idc = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	comuna = models.CharField(max_length=50)
	telefono = models.IntegerField()
	email = models.EmailField()
