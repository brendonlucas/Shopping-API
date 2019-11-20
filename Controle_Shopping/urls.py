from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('usuario.urls')),
    path('', include('loja.urls')),
]

