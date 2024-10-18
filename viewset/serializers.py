from rest_framework import serializers
from .models import *

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
    