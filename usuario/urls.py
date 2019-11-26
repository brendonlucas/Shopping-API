from django.conf.urls import url
from django.urls import path, include
from usuario import views
from usuario.views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('root', ApiRoot.as_view(), name=ApiRoot.name),
    # path('lojas/<int:id_loja>/funcionarios', views.funcionarios_list, name='list_loja_funcionarios'),
    path('lojas/<int:id_loja>/funcionarios/', LojaFuncionariosList.as_view(), name='list_loja_funcionarios'),
    path('lojas/<int:id_loja>/funcionarios/<int:id_funcionario/>', LojaFuncionarioDetalhes.as_view(), name='Detalhe_loja_funcionario'),

    path('admin/funcionarios/', FuncionariosList.as_view(), name='list_funcionarios'),
    path('admin/funcionarios/<int:id_funcionario>/', FuncionariosDetalhes.as_view(), name='Detalhes_funcionarios'),

    # path('clientes/', views.clientes_list, name='list_clientes'),
    path('clientes/', ClienteList.as_view(), name='list_clientes'),
    path('clientes/<int:id_cliente>/', ClienteDetalhes.as_view(), name='list_clientes'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


]
