from django.db import models


class Loja(models.Model):
    name = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)


class Produto(models.Model):
    name = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='loja')


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
