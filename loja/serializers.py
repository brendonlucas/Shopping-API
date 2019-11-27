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


class CompraClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('name', 'cpf')


class CompraProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('name', 'valor')


class AddCompraSerializer(serializers.ModelSerializer):
    cliente = CompraClienteSerializer()

    class Meta:
        model = Compra
        fields = ('cliente', 'quantidade')


"""
{
    "cliente": {
        "name": "Lucas",
        "cpf": "123456789"
    },
    "quantidade": 3
}
"""

class VerifyCompraSerializer(serializers.ModelSerializer):
    cliente = CompraClienteSerializer()

    class Meta:
        model = Compra
        fields = ('cliente', 'quantidade')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('name', 'cpf', 'telefone', 'endereco',)


class VendasSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    produto = ProdutoSerializer()

    class Meta:
        model = Compra
        fields = ('cliente', 'produto', 'quantidade', 'valor_total', 'data_compra')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class AddClienteSerializer(serializers.ModelSerializer):
    cliente_complement = UserSerializer()

    class Meta:
        model = Cliente
        fields = ('name', 'cpf', 'telefone', 'endereco', 'email', 'cliente_complement')

    def create(self, validated_data):
        name = validated_data.get('name')
        cpf = validated_data.get('cpf')
        telefone = validated_data.get('telefone')
        endereco = validated_data.get('endereco')
        email = validated_data.get('email')
        cliente_complemento = validated_data.get('cliente_complement')
        username = cliente_complemento['username']
        password = cliente_complemento['password']
        user = User.objects.create_user(username=username, password=password, email=email)
        cliente = Cliente.objects.create(name=name, cpf=cpf, telefone=telefone, endereco=endereco, email=email,
                                         cliente_complement=user)
        return validated_data


"""
{
    "name": "Josias Lima",
    "cpf": "45678913287",
    "telefone": "99885544",
    "endereco": "Rua alameda pereira",
    "email": "josias@gmail.com",
    "cliente_complement": {
        "username": "Josias",
        "password": "123456789"
    }
}
"""
