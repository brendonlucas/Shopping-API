from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')

urlpatterns = [
    url('', include('usuario.urls')),
    url('', include('loja.urls')),
    url(r'', schema_view)
]
