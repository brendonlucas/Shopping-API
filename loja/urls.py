from django.urls import path
from loja import views

urlpatterns = [
    path('lojas/', views.lojas_list, name='list_lojas'),
    path('lojas/<int:id_loja>/produtos/', views.produtos_list, name='list_produtos'),
]