from django.db import models

# Create your models here.

class Contatos(models.Model):

    Nome = models.CharField(max_length=200)
    Sobre_Nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    Tel = models.CharField(max_length=12)
    Email = models.EmailField(max_length=200)
