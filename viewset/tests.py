from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import *
from .factories import *
from decimal import Decimal

class ProductTestCase(TestCase):
    fixtures = ['products.json']
    
class ProductTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.products = ProductFactory.create_batch(5)
        self.product_list_url = reverse('product-list') 

    def test_product_creation(self):
        """Test that products are created correctly"""
        product_count = product.objects.count()
        self.assertEqual(product_count, 5)
        for p in self.products:
            self.assertIsInstance(p.name, str)
            self.assertIsInstance(p.price, Decimal)
            self.assertTrue(0 <= p.rating <= 5)

    
    def test_list_products(self):
        """Test listing all products"""
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_retrieve_single_product(self):
        """Test retrieving a single product"""
        product_instance = self.products[0]
        url = reverse('product-detail', kwargs={'pk': product_instance.pk})  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], product_instance.name)
        self.assertEqual(Decimal(response.data['price']), product_instance.price)
        self.assertEqual(float(response.data['rating']), product_instance.rating)    

    