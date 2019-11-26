from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics, pagination
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework import mixins
from loja.models import Loja
from loja.serializers import *
from rest_framework.pagination import LimitOffsetPagination
import django_filters.rest_framework
from rest_framework import filters


class LojasList(generics.ListAPIView):
    queryset = Loja.objects.all()
    serializer_class = LojasSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['name', 'id']
    # filterset_fields = ['name', 'local']

    def get(self, request, *args, **kwargs):
        lojas = Loja.objects.all()
        lojas_serializer = LojasSerializer(lojas, many=True)
        return self.list(lojas_serializer.data, *args, **kwargs)
        # return Response(lojas_serializer.data)

    def post(self, request, *args, **kwargs):
        lojas_serializer = LojasSerializer(data=request.data)
        if lojas_serializer.is_valid():
            lojas_serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)


class LojaDetalhes(generics.GenericAPIView):
    queryset = Loja.objects.all()
    serializer_class = LojasSerializer

    def get(self, request, id_loja, *args, **kwargs):
        lojas = Loja.objects.get(id=id_loja)
        lojas_serializer = LojasSerializer(lojas)
        return Response(lojas_serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProdutosList(generics.GenericAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'id']
    pagination_class = PageNumberPagination

    def get(self, request, id_loja, *args, **kwargs):
        try:
            loja = Loja.objects.get(id=id_loja)
        except Loja.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

        produtos = Produto.objects.filter(loja=id_loja)
        # produtos_serializer = ProdutoSerializer(produtos, many=True)
        page = self.paginate_queryset(produtos)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request, id_loja, *args, **kwargs):
        try:
            loja = Loja.objects.get(id=id_loja)
        except Loja.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

        produto_serializer = ProdutoSerializer(data=request.data)
        if produto_serializer.is_valid():
            name = request.data['name']
            quantidade = request.data['quantidade']
            valor = request.data['valor']
            loja = Loja.objects.get(id=id_loja)
            Produto.objects.create(name=name, quantidade=quantidade, valor=valor, loja=loja)
            return Response(request.data, status=status.HTTP_201_CREATED)


class ProdutoDetalhes(generics.GenericAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get(self, request, id_loja, id_produto, *args, **kwargs):
        try:
            loja = Loja.objects.get(id=id_loja)
            produtos = Produto.objects.filter(loja=id_loja)
            if id_produto <= len(produtos):
                produto = produtos[id_produto - 1]
            else:
                return Response({'erro': '404_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)
        except Loja.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

        produto_serializer = ProdutoSerializer(produto)
        return Response(produto_serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProdutoCompra(generics.GenericAPIView):
    queryset = Compra.objects.all()
    serializer_class = AddCompraSerializer

    def post(self, request, id_loja, id_produto, *args, **kwargs):
        try:
            loja = Loja.objects.get(id=id_loja)
            produtos = Produto.objects.filter(loja=id_loja)
            if id_produto <= len(produtos):
                produto = produtos[id_produto - 1]
            else:
                return Response({'erro': '404_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)
        except Loja.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

        dados_serializer = VerifyCompraSerializer(data=request.data)
        if dados_serializer.is_valid():
            try:
                cliente = Cliente.objects.get(cpf=request.data['cliente']['cpf'])
                if cliente.name != request.data['cliente']['name']:
                    return Response({'erro': "Name Cliente HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)
            except Cliente.DoesNotExist:
                return Response({'erro': "Cliente HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

            valor_total = produto.valor * request.data['quantidade']
            c = Compra(cliente=cliente, produto=Produto.objects.get(id=produto.id), loja=loja,
                       quantidade=request.data['quantidade'],
                       valor_total=valor_total)
            c.save()
            compra_serializer = AddCompraSerializer(c)

            return Response(compra_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


class VendaLoja(generics.GenericAPIView):
    queryset = Compra.objects.all()
    serializer_class = VendasSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['valor_total', 'id']

    # filterset_fields = ['name', 'local']

    def get(self, request, id_loja, *args, **kwargs):
        try:
            loja = Loja.objects.get(id=id_loja)
        except Loja.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

        vendas = Compra.objects.filter(loja=id_loja)
        # produtos_serializer = VendasSerializer(vendas, many=True)

        page = self.paginate_queryset(vendas)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(vendas, many=True)
        return Response(serializer.data)
        # return Response(produtos_serializer.data)


"""
class P(generics.GenericAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get(self, request, id_loja, *args, **kwargs):
        pass

    def post(self, request, id_loja, *args, **kwargs):
        pass
"""
