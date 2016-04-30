from django.conf.urls import url,include,patterns
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from views import holamundo
from wak.views import IndexView

urlpatterns = patterns(
    'api.views',
    url(r'^holamundo/$', 'holamundo'),
    url(r'^categorias/$', 'categoria'),

)
