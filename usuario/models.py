from django.contrib.auth.models import User
from django.db import models

from loja.models import Loja


class Funcionario(models.Model):
    name = models.CharField(max_length=250)
    cpf = models.CharField(max_length=30)
    cargo = models.CharField(max_length=250)
    telefone = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    funcionario_complement = models.OneToOneField(User, on_delete=models.CASCADE, related_name='complemento')
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='Loja_pertencente')


class Cliente(models.Model):
    name = models.CharField(max_length=250)
    cpf = models.CharField(max_length=30)
    telefone = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    cliente_complement = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente_complement')
