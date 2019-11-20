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

