
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from shop.models import Category, Product
from shop.pagination import ProductPagination
from shop.serializers import CategorySerializer, ProductSerializer

def index(request):
    return HttpResponse("Under construction - index.")

@api_view(['GET'])
@permission_classes([AllowAny])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def getProducts(request):
    category_id = request.query_params.get('category_id')

    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()

    paginator = ProductPagination()
    product_subset = paginator.paginate_queryset(products, request)
    
    serializer = ProductSerializer(product_subset, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def getProduct(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)