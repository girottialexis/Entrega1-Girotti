from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField(primary_key=True)
    
class Equipo(models.Model):
    modelo_equipo = models.CharField(max_length=40)
    numero_telefono = models.IntegerField(primary_key=True)
    
class Fichatecnica(models.Model):
    numero_ficha = models.IntegerField(primary_key=True)
    fecha_recibido = models.DateField()
    problema_tecnico = models.CharField(max_length=300)
    reparado = models.BooleanField()
    fecha_entregado = models.DateField(0000-00-00)