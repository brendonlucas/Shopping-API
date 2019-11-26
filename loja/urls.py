from django.urls import path

from loja import views
from loja.views import *

urlpatterns = [
    # path('lojas/', views.lojas_list, name='list_lojas'),
    path('lojas/', LojasList.as_view(), name='list_lojas'),
    path('lojas/<int:id_loja>/', LojaDetalhes.as_view(), name='Detalhes_lojas'),

    # path('lojas/<int:id_loja>/produtos/', views.produtos_list, name='list_produtos'),
    path('lojas/<int:id_loja>/produtos/', ProdutosList.as_view(), name='list_produtos'),

    # path('lojas/<int:id_loja>/produtos/<int:id_produto>/', views.produto_detalhes, name='detalhes_produto'),
    path('lojas/<int:id_loja>/produtos/<int:id_produto>/', ProdutoDetalhes.as_view(), name='detalhes_produto'),

    # path('lojas/<int:id_loja>/produtos/<int:id_produto>/compra/', views.produto_compra, name='compra_produto'),
    path('lojas/<int:id_loja>/produtos/<int:id_produto>/compra/', ProdutoCompra.as_view(), name='compra_produto'),

    # path('lojas/<int:id_loja>/vendas/', views.vendas_loja, name='vendas_loja'),
    path('lojas/<int:id_loja>/vendas/', VendaLoja.as_view(), name='vendas_loja'),

]
