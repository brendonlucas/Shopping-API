from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from loja.models import Cliente
from loja.serializers import *
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


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'info': reverse('list_lojas', request=request),

        }, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def clientes_list(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            clientes = Cliente.objects.all()
            clientes_serializer = ClienteSerializer(clientes, many=True)
            return Response(clientes_serializer.data)
        else:
            return Response({'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'POST':
        cliente_serializer = AddClienteSerializer(data=request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cliente_detalhes(request,id_cliente):
    return Response(status=status.HTTP_200_OK)