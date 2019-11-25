from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from loja.models import Cliente
from loja.serializers import *
from usuario.models import Funcionario
from usuario.serializers import *


class FuncionariosList(generics.GenericAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = AddFuncionarioSerializer

    def get(self, request, *args, **kwargs):
        funcionarios = Funcionario.objects.all()
        funcionarios_serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(funcionarios_serializer.data)

    def post(self, request, id_loja, *args, **kwargs):
        funcionarios_serializer = AddFuncionarioSerializer(data=request.data)
        if funcionarios_serializer.is_valid():
            funcionarios_serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)


class FuncionariosDetalhes(generics.GenericAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def get(self, request, id_funcionario, *args, **kwargs):
        try:
            funcionario = Funcionario.objects.get(id=id_funcionario)
        except Funcionario.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

        funcionarios_serializer = FuncionarioSerializer(funcionario, many=True)
        return Response(funcionarios_serializer.data)

    def put(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class LojaFuncionariosList(generics.GenericAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = AddFuncionarioSerializer

    def get(self, request,id_loja, *args, **kwargs):
        try:
            loja = Loja.objects.get(id=id_loja)
        except Loja.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

        funcionarios = Funcionario.objects.filter(loja=id_loja)
        funcionarios_serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(funcionarios_serializer.data)

    def post(self, request, id_loja, *args, **kwargs):
        try:
            loja = Loja.objects.get(id=id_loja)
        except Loja.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

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


class LojaFuncionarioDetalhes(generics.GenericAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = AddFuncionarioSerializer

    def get(self, request, id_loja, id_funcionario, *args, **kwargs):
        try:
            loja = Loja.objects.get(id=id_loja)
            funcionarios = Funcionario.objects.filter(loja=id_loja)
            if id_funcionario <= len(funcionarios):
                funcionario = funcionarios[id_funcionario - 1]
            else:
                return Response({'erro': '404_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)
        except Funcionario.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

        # funcionario = Funcionario.objects.filter(loja=id_loja)
        funcionario_serializer = FuncionarioSerializer(funcionario)
        return Response(funcionario_serializer.data)

    def put(self, request, id_loja,id_funcionario, *args, **kwargs):
        pass

    def delete(self, request, id_loja,id_funcionario, *args, **kwargs):
        pass


class ClienteList(generics.GenericAPIView):
    queryset = Cliente.objects.all()
    serializer_class = AddClienteSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            clientes = Cliente.objects.all()
            clientes_serializer = ClienteSerializer(clientes, many=True)
            return Response(clientes_serializer.data)
        else:
            return Response({'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        cliente_serializer = AddClienteSerializer(data=request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetalhes(generics.GenericAPIView):
    queryset = Cliente.objects.all()
    serializer_class = AddClienteSerializer

    def get(self, request, id_cliente, *args, **kwargs):
        if request.user.is_authenticated:
            clientes = Cliente.objects.get(id=id_cliente)
            clientes_serializer = ClienteSerializer(clientes, many=True)
            return Response(clientes_serializer.data)
        else:
            return Response({'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, id_loja, *args, **kwargs):
        pass

    def delete(self, request, id_loja, *args, **kwargs):
        pass


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'info': reverse('list_lojas', request=request),

        }, status=status.HTTP_200_OK)


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
