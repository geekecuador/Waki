from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CategoriaSerializer
from wak.models import Categoria


class HolaMundo(APIView):
    def get(self, request, format=None):
        return Response({'nombre':'Hola mundo'})

holamundo = HolaMundo.as_view()


class Categorias(APIView):
    serializer_class = CategoriaSerializer
    def get(self, request, format=None):
        categoria = Categoria.objects.all()
        response = self.serializer_class(categoria, many=True)
        return Response(response.data)

categoria = Categorias.as_view()
