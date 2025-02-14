
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from shop.models import Product
from shop.serializers import ProductSerializer

def index(request):
    return HttpResponse("Under construction - index.")

@api_view(['GET'])
@permission_classes([AllowAny])
def getCategories(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

def getProducts(request):
    return HttpResponse("Under construction - get all products.")

def getProduct(request, id):
    return HttpResponse("Under construction - get product by id.")