from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from usuario.models import Funcionario
from usuario.serializers import *


@api_view(['GET', 'POST'])
def funcionarios_view(request):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()
        funcionarios_serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(funcionarios_serializer.data)
    if request.method == 'POST':
        funcionarios_serializer = AddFuncionarioSerializer(data=request.data)
        if funcionarios_serializer.is_valid():
            funcionarios_serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def funcionarios_list(request, id_loja):
    try:
        loja = Loja.objects.get(id=id_loja)
    except Loja.DoesNotExist:
        return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        funcionarios = Funcionario.objects.filter(loja=id_loja)
        funcionarios_serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(funcionarios_serializer.data)

    if request.method == 'POST':
        funcionarios_serializer = AddFuncionarioSerializer(data=request.data)
        if funcionarios_serializer.is_valid():
            name = request.data['name']
            cpf = request.data['cpf']
            telefone = request.data['telefone']
            endereco = request.data['endereco']
            cargo = request.data['cargo']
            username = request.data['complemento']['username']
            password = request.data['complemento']['password']
            email = request.data['complemento']['email']
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email)
            Funcionario.objects.create(name=name,
                                       cpf=cpf,
                                       telefone=telefone,
                                       endereco=endereco,
                                       cargo=cargo,
                                       funcionario_complement=user,
                                       loja=loja)
            return Response(request.data, status=status.HTTP_201_CREATED)



