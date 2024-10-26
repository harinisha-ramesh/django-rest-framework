from rest_framework import serializers
from .models import *

class Productserializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True,max_length=10,
                                 error_messages={
                                    'required': 'name: This Feild is required',
                                    'max_length': 'The maximum length should be 10 characters '
                                 })
    price = serializers.DecimalField(required=True,max_digits=10, decimal_places=3,
                                    error_messages={
                                    'required': 'price: This Feild is required',
                                    'max_digits': 'The maximum digit should be 10 characters ',
                                    'invalid': 'price: The price must be a valid decimal number'
                                 })
    rating = serializers.FloatField(required=False,default=0,
                                    error_messages={
                                        'invalid': 'rating: rating should be in a Float number'
                                    })
    class Meta:
        model = product
        fields = '__all__'

  

    