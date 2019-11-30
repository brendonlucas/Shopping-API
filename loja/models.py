from django.contrib.auth.models import User
from django.db import models


class Loja(models.Model):
    name = models.CharField(max_length=255)
    andar = models.CharField(max_length=255)
    lote = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)


class Produto(models.Model):
    name = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='loja')


class Cliente(models.Model):
    name = models.CharField(max_length=250)
    cpf = models.CharField(max_length=30)
    telefone = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    email = models.CharField(max_length=250)


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produto')
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='compra_loja')
    quantidade = models.IntegerField()
    valor_total = models.FloatField()
    data_compra = models.DateField(auto_now_add=True)
