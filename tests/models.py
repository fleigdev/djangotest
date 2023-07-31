from django.db import models

class Producto(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Empleado(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class Cliente(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()