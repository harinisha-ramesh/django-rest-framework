from rest_framework import serializers
from .models import *

class Product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Product_serializer2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name','product_code']       

class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'        