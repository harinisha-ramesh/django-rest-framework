from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import * 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication

class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = Productserializer
    authentication_classes = [BasicAuthentication]  # Authenticate with username/password
    permission_classes = [IsAuthenticatedOrReadOnly]

# from rest_framework import viewsets
# from rest_framework.response import Response
# from .models import Product
# from .serializers import ProductSerializer

# class ProductViewSet(viewsets.ViewSet):
    # def list(self, request):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data )
    #     return Response(serializer.errors)

    # def retrieve(self, request, pk=None):
    #     product = Product.objects.get(pk=pk)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     product = Product.objects.get(pk=pk)
    #     serializer = ProductSerializer(product, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # def destroy(self, request, pk=None):
    #     product = Product.objects.get(pk=pk)
    #     product.delete()
       
