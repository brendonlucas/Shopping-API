from rest_framework import serializers
from usuario.models import *


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('id', 'name', 'cpf', 'telefone', 'endereco', 'cargo')


class AddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ('name',)


class AddFuncionarioSerializer(serializers.ModelSerializer):
    complemento = AddUserSerializer()

    class Meta:
        model = Funcionario
        fields = ('name', 'cpf', 'telefone', 'endereco', 'cargo', 'complemento')

    def create(self, validated_data):
        name = validated_data.get('name')
        cpf = validated_data.get('cpf')
        telefone = validated_data.get('telefone')
        endereco = validated_data.get('endereco')
        cargo = validated_data.get('cargo')
        funcionario_complement = validated_data.get('funcionario_complement')
        username = funcionario_complement['username']
        password = funcionario_complement['password']
        email = funcionario_complement['email']
        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email)
        Funcionario.objects.create(name=name,
                                   cpf=cpf,
                                   telefone=telefone,
                                   endereco=endereco,
                                   cargo=cargo,
                                   funcionario_complement=user)
        return validated_data


"""
{
    "name": "lucas Silva",
    "cpf": "123456789",
    "telefone": "99885545",
    "endereco": "Rua antonio neiova",
    "cargo": "Chefe",
    "complemento": {
        "username": "Lucas",
        "password": "123456789",
        "email": "brendonplay@gmail.com"
    }
}
"""
