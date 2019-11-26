from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from loja.models import Cliente
from loja.serializers import *
from usuario.models import Funcionario
from usuario.serializers import *
from rest_framework import filters


class FuncionariosList(generics.ListAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter]
    ordering_fields = ['name', 'id']
    filterset_fields = ['name', 'cargo']
    search_fields = ['name', 'endereco', 'cpf']

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            funcionarios = Funcionario.objects.all()
            funcionarios_serializer = FuncionarioSerializer(funcionarios, many=True)
            return self.list(funcionarios_serializer.data, *args, **kwargs)
        else:
            return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)


class FuncionariosDetalhes(generics.GenericAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def get(self, request, id_funcionario, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            try:
                funcionario = Funcionario.objects.get(id=id_funcionario)
            except Funcionario.DoesNotExist:
                return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

            funcionarios_serializer = FuncionarioSerializer(funcionario)
            return Response(funcionarios_serializer.data)
        else:
            return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)


class LojaFuncionariosList(generics.GenericAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = AddFuncionarioSerializer

    def get(self, request, id_loja, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                loja = Loja.objects.get(id=id_loja)
            except Loja.DoesNotExist:
                return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

            funcionario = Funcionario.objects.get(funcionario_complement=request.user.id)
            if funcionario.loja == loja or request.user.is_staff:
                funcionarios = Funcionario.objects.filter(loja=id_loja)
                # funcionarios_serializer = FuncionarioSerializer(funcionarios, many=True)

                page = self.paginate_queryset(funcionarios)
                if page is not None:
                    serializer = FuncionarioSerializer(page, many=True)
                    return self.get_paginated_response(serializer.data)
                serializer = FuncionarioSerializer(funcionarios, many=True)

                return Response(serializer.data)
                # return Response(funcionarios_serializer.data)
            else:
                return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, id_loja, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                loja = Loja.objects.get(id=id_loja)
            except Loja.DoesNotExist:
                return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

            loja = Loja.objects.get(id=id_loja)
            funcionario = Funcionario.objects.get(funcionario_complement=request.user.id)
            if funcionario.loja == loja or request.user.is_staff:
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
                else:
                    return Response({'erro': 'HTTP_400_BAD_REQUEST / Json not valid'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)


class LojaFuncionarioDetalhes(generics.GenericAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def get(self, request, id_loja, id_funcionario, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                loja = Loja.objects.get(id=id_loja)
                funcionarios = Funcionario.objects.filter(loja=id_loja)
                if id_funcionario <= len(funcionarios):
                    funcionario = funcionarios[id_funcionario - 1]
                else:
                    return Response({'erro': '404_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)
            except Funcionario.DoesNotExist:
                return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

            funcionario_logado = Funcionario.objects.get(funcionario_complement=request.user.id)
            if funcionario_logado.loja == loja or request.user.is_staff:
                # funcionario = Funcionario.objects.filter(loja=id_loja)
                funcionario_serializer = FuncionarioSerializer(funcionario)
                return Response(funcionario_serializer.data)
            else:
                return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, id_loja, id_funcionario, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                loja = Loja.objects.get(id=id_loja)
                funcionarios = Funcionario.objects.filter(loja=id_loja)
                if id_funcionario <= len(funcionarios):
                    funcionario = funcionarios[id_funcionario - 1]
                else:
                    return Response({'erro': '404_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)
            except Funcionario.DoesNotExist:
                return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

            loja = Loja.objects.get(id=id_loja)
            funcionario_logado = Funcionario.objects.get(funcionario_complement=request.user.id)
            funcionario_serializer = FuncionarioSerializer(data=request.data)

            if funcionario_logado.loja == loja or request.user.is_staff:
                if funcionario_serializer.is_valid():
                    funcionario.name = request.data['name']
                    funcionario.cargo = request.data['cargo']
                    funcionario.endereco = request.data['endereco']
                    funcionario.telefone = request.data['telefone']
                    funcionario.cpf = request.data['cpf']
                    funcionario.save()
                    return Response(request.data, status=status.HTTP_200_OK)
                else:
                    return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, id_loja, id_funcionario, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                loja = Loja.objects.get(id=id_loja)
                funcionarios = Funcionario.objects.filter(loja=id_loja)
                if id_funcionario <= len(funcionarios):
                    funcionario = funcionarios[id_funcionario - 1]
                else:
                    return Response({'erro': '404_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)
            except Funcionario.DoesNotExist:
                return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

            loja = Loja.objects.get(id=id_loja)
            funcionario_logado = Funcionario.objects.get(funcionario_complement=request.user.id)
            if funcionario_logado.loja == loja or request.user.is_staff:
                funcionario.delet()
                return Response({'Info': 'Item has be deleted'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'erro': 'HTTP_401_UNAUTHORIZED'}, status=status.HTTP_401_UNAUTHORIZED)


class ClienteList(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = AddClienteSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter]
    ordering_fields = ['name', 'id']
    filterset_fields = ['name']
    search_fields = ['name', 'endereco', 'cpf']

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            clientes = Cliente.objects.all()
            clientes_serializer = ClienteSerializer(clientes, many=True)
            return self.list(clientes_serializer.data, *args, **kwargs)
        else:
            return Response({'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cliente_serializer = AddClienteSerializer(data=request.data)
            if cliente_serializer.is_valid():
                cliente_serializer.save()
                return Response(request.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'erro': 'Json invalid'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


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


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'info': reverse('list_lojas', request=request),

        }, status=status.HTTP_200_OK)
