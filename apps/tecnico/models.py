from django.db import models

# Create your models here.

class Tecnico(models.Model):
	idt = models.CharField(max_length=10, primary_key=True)
	email = models.EmailField()
	contraseña = models.CharField(max_length=30)
