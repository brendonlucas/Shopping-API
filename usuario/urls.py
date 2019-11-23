from django.urls import path
from usuario import views
from usuario.views import *

urlpatterns = [
    # path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('lojas/<int:id_loja>/funcionarios', views.funcionarios_list, name='list_loja_funcionarios'),
    path('clientes/', views.clientes_list, name='list_clientes'),
    path('clientes/<int:id_cliente>/', views.cliente_detalhes, name='detalhes_clientes'),
]
