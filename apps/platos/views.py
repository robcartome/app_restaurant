from django.shortcuts import render
from django.db.models import Q
from .models import Platos

# Serializador
from django.core import serializers as srr

# DRF
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.platos.serializers import PlatosSerializer

# Create your views here.
def platos_list(request):
    data_context = Platos.objects.all()
    print(data_context)
    return render(request, 'platos/platos_list.html', context={'data': data_context})

def plato_details(request):

    return render(request, 'platos/plato_detail.html', {})

def plato_search(request):
    query = request.GET.get('q', '')
    print("query: {}".format(query))
    results = (
        Q(nombre__icontains=query)
    )
    print("resuts: {}".format(results))
    data_context = Platos.objects.filter(results).distinct()

    return render(request, 'platos/plato_search.html', context={'data': data_context, "query": query})


# REST
@api_view(['GET', 'DELETE'])
def plato_api_view(request, pk):
    plato = Platos.objects.filter(id=pk).first()

    if plato:
        if request.method == 'GET':
            serializers_class = PlatosSerializer(plato)

            return Response(serializers_class.data)

        elif request.method == 'DELETE':
            plato.delete()
            return Response('Plato se ha eliminado correctamente', status=status.HTTP_201_CREATED)

    return Response({'message': 'No se ha encontrado ningún plato con estos datos'}, status = status.HTTP_400_BAD_REQUEST)