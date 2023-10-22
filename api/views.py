import json
from website.models import *
from website.serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.scrappers.Lojas.KabumScrapper import KabumScrapper
from api.scrappers.Lojas.TerabyteScrapper import TerabyteScrapper

# Global variables
driverName = "firefox"

@api_view(['GET', 'POST'])
def kabum_list(request, format=None):
    if request.method == 'GET':
        data = Produto.objects.all()
        serializer = ProdutoSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = get_plataforma_loja("Kabum")
        scrapperResponse = KabumScrapper(driverName, data).manager()

        serializer = ProdutoSerializer(data=scrapperResponse, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def terabyte_list(request, format=None):
    if request.method == 'GET':
        data = Produto.objects.all()
        serializer = ProdutoSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = get_plataforma_loja("Terabyte")
        scrapperResponse = TerabyteScrapper(driverName, data).manager()

        serializer = ProdutoSerializer(data=scrapperResponse, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def plataforma_e_loja(request, format=None):
    if request.method == 'GET':
        plataformaData = Plataforma.objects.all()
        lojaData = Loja.objects.all()

        plataformaSerializer = PlataformaSerializer(plataformaData, many=True)
        lojaSerializer = LojaSerializer(lojaData, many=True)
        
        data = {
            "P": plataformaSerializer.data,
            "L": lojaSerializer.data
        }
        return Response(data)
    
    elif request.method == "POST":
        plataformaSerializer = PlataformaSerializer(data=[
            {"nome": 'Computador'},
            {"nome": 'PlayStation'},
            {"nome": 'Xbox'},
            {"nome": 'Nintendo'},
        ], many=True)

        lojaSerializer = LojaSerializer(data=[
            {"nome": 'Steam'},
            {"nome": 'Nuuvem'},
            {"nome": 'GoG'},
            {"nome": 'Epic Games'},
            {"nome": 'Buscapé'},
            {"nome": 'Zoom'},
            {"nome": 'Americanas'},
            {"nome": 'Magazine L.'},
            {"nome": 'Submarino'},
            {"nome": 'Casas Bahia'},
            {"nome": 'Kabum'},
            {"nome": 'Terabyte'},
        ], many=True)

        if plataformaSerializer.is_valid() and lojaSerializer.is_valid():
            plataformaSerializer.save()
            lojaSerializer.save()
            return Response({
                "plataforma": plataformaSerializer.data,
                "loja": lojaSerializer.data
            }, status=status.HTTP_201_CREATED) 
        return Response({
            "plataforma": plataformaSerializer.errors,
            "loja": lojaSerializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

def get_plataforma_loja(loja):
    plataformaData = Plataforma.objects.all()
    lojaData = Loja.objects.filter(nome=loja)

    plataformaSerializer = PlataformaSerializer(plataformaData, many=True)
    lojaSerializer = LojaSerializer(lojaData, many=True)
    
    data = {
        "P": json.loads(json.dumps(plataformaSerializer.data)),
        "L": json.loads(json.dumps(lojaSerializer.data))[0]["id"]
    }
    return data
