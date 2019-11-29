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
    # cliente_complement = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente_complement')
# s = Cliente(name='Lucas',cpf='123456789',telefone='99663322',endereco='rua sem volta',email='lucas123@gmail.com')


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produto')
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='compra_loja')
    quantidade = models.IntegerField()
    valor_total = models.FloatField()
    data_compra = models.DateField(auto_now_add=True)
# c = Compra(cliente=s,produto=Produto.objects.get(id=1),loja=Loja.objects.get(id=2),quantidade=2,valor_total=5500)

"""
{
    "name": "Tv 45 polegadas LG",
    "quantidade": 10,
    "valor": 1500,
}
"""

"""
{
    "name": "Paraiba",
    "local": "Piso 3 loja 5",
    "cnpj": "789456123"
}
"""
