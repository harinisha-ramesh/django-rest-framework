from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product


class ProductView(APIView):

    def get(self, request):
        all_products = Product.objects.all()
        product_data = []
        for products in all_products:
            single_product = {
                "id" : products.id,
                "product_name" : products.product_name,
                "product_code" : products.product_code,
                "price" : products.price,
                "rating" : products.rating
            }
            product_data.append(single_product)
        return Response(product_data)    

    def post(self, request):
        
        new_product = Product(product_name = request.data['product_name'], product_code = request.data['product_code'], price = request.data['price'], rating = request.data['rating'])

        new_product.save()
        
        return Response("Data Saved")


class ProductViewById(APIView):

    def get(self, request, id):
        product = Product.objects.get(id = id)
        single_product = {
                "id" : product.id,
                "product_name" : product.product_name,
                "product_code" : product.product_code,
                "price" : product.price,
                "rating" : product.rating
            }
        return Response(single_product)    
    
    def put(self, request, id):
        product = Product.objects.filter(id = id)
        product.update(product_name = request.data['product_name'], product_code = request.data['product_code'], price = request.data['price'], rating = request.data['rating'])
        return Response("Data Updated")
    
    def delete(self, request, id):
        product = Product.objects.get(id = id)
        product.delete()
        return Response("Data Deleted")  