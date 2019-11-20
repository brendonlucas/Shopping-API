from django.urls import path

from usuario import views

urlpatterns = [
    # path('funcionarios/', views.funcionarios_view, name='list_funcionarios'),
    path('lojas/<int:id_loja>/funcionarios', views.funcionarios_list, name='list_loja_funcionarios')
]