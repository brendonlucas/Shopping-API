from django.urls import path
from loja import views

urlpatterns = [
    path('lojas/', views.lojas_list, name='list_lojas'),
    path('lojas/<int:id_loja>/produtos/', views.produtos_list, name='list_produtos'),
    path('lojas/<int:id_loja>/produtos/<int:id_produto>/', views.produto_detalhes, name='detalhes_produto'),
    path('lojas/<int:id_loja>/produtos/<int:id_produto>/compra/', views.produto_compra, name='compra_produto'),
    path('lojas/<int:id_loja>/vendas/', views.vendas_loja, name='vendas_loja'),

]