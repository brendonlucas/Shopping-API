from django.urls import path
from usuario import views
from usuario.views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('root', ApiRoot.as_view(), name=ApiRoot.name),
    path('lojas/<int:id_loja>/funcionarios', views.funcionarios_list, name='list_loja_funcionarios'),
    path('clientes/', views.clientes_list, name='list_clientes'),
    path('clientes/<int:id_cliente>/', views.cliente_detalhes, name='detalhes_clientes'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
