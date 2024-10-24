from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import * 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication
# import logging
# import pdb

# logger = logging.getLogger('viewset')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all() 
    serializer_class = Productserializer
    authentication_classes = [BasicAuthentication]  
    permission_classes = [IsAuthenticatedOrReadOnly]

class MyReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = product.objects.all()
    serializer_class = Productserializer

    # def list(self, request, *args, **kwargs):
        # pdb.set_trace()  # Set a breakpoint here to debug the list view
        # return super().list(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
        # pdb.set_trace()  # Set a breakpoint here to debug the create view
        # return super().create(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
        # pdb.set_trace()  # Set a breakpoint here to debug the retrieve view
        # return super().retrieve(request, *args, **kwargs)
    
    # def list(self, request, *args, **kwargs):
        # logger.info("Fetching product list")  # Log info message
        # response = super().list(request, *args, **kwargs)
        # logger.debug(f"Response: {response.data}")  # Log debug message
        # return response

    # def create(self, request, *args, **kwargs):
        # logger.info("Creating a new product")  # Log info message
        # response = super().create(request, *args, **kwargs)
        # logger.debug(f"Created product: {response.data}")  # Log debug message
        # return response

    # def update(self, request, *args, **kwargs):
        # logger.info("Updating a product")  # Log info message
        # response = super().update(request, *args, **kwargs)
        # logger.debug(f"Updated product: {response.data}")  # Log debug message
        # return response

    # def destroy(self, request, *args, **kwargs): 
        # logger.warning("Deleting a product")  # Log warning message
        # response = super().destroy(request, *args, **kwargs)
        # logger.debug(f"Deleted product: {response.data}")  # Log debug message
        # return response

# from rest_framework import viewsets
# from rest_framework.response import Response                                                                                                                                                                                                                                                                                                                     

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
       
