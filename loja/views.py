from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from loja.models import Loja
from loja.serializers import *


@api_view(['GET', 'POST'])
def lojas_list(request):
    if request.method == 'GET':
        lojas = Loja.objects.all()
        lojas_serializer = LojasSerializer(lojas, many=True)
        return Response(lojas_serializer.data)
    if request.method == 'POST':
        lojas_serializer = LojasSerializer(data=request.data)
        if lojas_serializer.is_valid():
            lojas_serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def produtos_list(request, id_loja):
    try:
        loja = Loja.objects.get(id=id_loja)
    except Loja.DoesNotExist:
        return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        produtos = Produto.objects.filter(loja=id_loja)
        produtos_serializer = ProdutoSerializer(produtos, many=True)
        return Response(produtos_serializer.data)

    if request.method == 'POST':
        produto_serializer = ProdutoSerializer(data=request.data)
        if produto_serializer.is_valid():
            name = request.data['name']
            quantidade = request.data['quantidade']
            valor = request.data['valor']
            loja = Loja.objects.get(id=id_loja)
            Produto.objects.create(name=name, quantidade=quantidade, valor=valor, loja=loja)
            return Response(request.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def produto_detalhes(request, id_loja, id_produto):
    try:
        loja = Loja.objects.get(id=id_loja)
        produtos = Produto.objects.filter(loja=id_loja)
        if id_produto <= len(produtos):
            produto = produtos[id_produto - 1]
        else:
            return Response({'erro': '404_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)
    except Loja.DoesNotExist:
        return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        produto_serializer = ProdutoSerializer(produto)
        return Response(produto_serializer.data)


@api_view(['POST'])
def produto_compra(request, id_loja, id_produto):
    try:
        loja = Loja.objects.get(id=id_loja)
        produtos = Produto.objects.filter(loja=id_loja)
        if id_produto <= len(produtos):
            produto = produtos[id_produto - 1]
        else:
            return Response({'erro': '404_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)
    except Loja.DoesNotExist:
        return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        dados_serializer = VerifyCompraSerializer(data=request.data)
        if dados_serializer.is_valid():
            try:
                cliente = Cliente.objects.get(cpf=request.data['cliente']['cpf'])
                if cliente.name != request.data['cliente']['name']:
                    return Response({'erro': "Name Cliente HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)
            except Cliente.DoesNotExist:
                return Response({'erro': "Cliente HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

            print('vaklidou')
            valor_total = produto.valor * request.data['quantidade']
            c = Compra(cliente=cliente, produto=Produto.objects.get(id=1), loja=loja, quantidade=request.data['quantidade'],
                           valor_total=valor_total)
            compra_serializer = AddCompraSerializer(c)
            return Response(compra_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def vendas_loja(request, id_loja):
    try:
        loja = Loja.objects.get(id=id_loja)
    except Loja.DoesNotExist:
        return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vendas = Compra.objects.filter(loja=id_loja)
        produtos_serializer = VendasSerializer(vendas, many=True)
        return Response(produtos_serializer.data)
