from rest_framework import serializers

from loja.models import *


class LojasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ('id', 'name', 'local', 'cnpj')


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'name', 'quantidade', 'valor')


class AddLojaProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ('name',)


class AddProdutoSerializer(serializers.ModelSerializer):
    loja = LojasSerializer()

    class Meta:
        model = Produto
        fields = ('name', 'quantidade', 'valor', 'loja')

    def create(self, validated_data):
        name = validated_data.get('name')
        quantidade = validated_data.get('quantidade')
        valor = validated_data.get('valor')
        loja = validated_data.get('loja')['name']
        # name_loja = loja['name']
        loja = Loja.objects.get(name=loja)
        Produto.objects.create(name=name, quantidade=quantidade, valor=valor, loja=loja)

        return validated_data
