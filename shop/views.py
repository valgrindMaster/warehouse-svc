
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Under construction - index.")

def getCategories(request):
    return HttpResponse("Under construction - get all categories.")

def getProducts(request):
    return HttpResponse("Under construction - get all products.")

def getProduct(request, id):
    return HttpResponse("Under construction - get product by id.")