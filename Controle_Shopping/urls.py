import rest_framework
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API - Shopping')

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('usuario.urls')),
    url('', include('loja.urls')),
    url(r'docs', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
