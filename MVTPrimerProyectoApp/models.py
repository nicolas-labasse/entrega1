from django.db import models

# Create your models here.


class Materias(models.Model):
    nombre = models.CharField(max_length=50)
    horas = models.IntegerField()


class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)
  
