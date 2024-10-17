from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class ProductView(APIView):

    # def get(self, request):
    #     all_products = Product.objects.all()
    #     product_data = []
    #     for products in all_products:
    #         single_product = {
    #             "id" : products.id,
    #             "product_name" : products.product_name,
    #             "product_code" : products.product_code,
    #             "price" : products.price,
    #             "rating" : products.rating,
    #             "category_id" : products.category_id
    #         }
    #         product_data.append(single_product)
    #     return Response(product_data)    
    
    def get(self, request):
        all_products = Product.objects.all()
        serialize_product = Product_serializer(all_products, many = True).data
        
        return Response(serialize_product)  
    
    # def post(self, request):
        
    #     new_product = Product(product_name = request.data['product_name'], product_code = request.data['product_code'], price = request.data['price'], rating = request.data['rating'], category_id = request.data[category_id])

    #     new_product.save()
        
    #     return Response("Data Saved")
    
    def post(self, request):
        
        new_product = Product_serializer(data=request.data)

        if new_product.is_valid():
            new_product.save()
            return Response("Data Saved")
        else:
            return Response(new_product.errors)
        

class ProductViewById(APIView):

    # def get(self, request, id):
    #     product = Product.objects.get(id = id)
    #     single_product = {
    #             "id" : product.id,
    #             "product_name" : product.product_name,
    #             "product_code" : product.product_code,
    #             "price" : product.price,
    #             "rating" : product.rating,
    #             "category_id" : product.category_id
    #         }
    #     return Response(single_product)    
    
    def get(self, request, id):
        product = Product.objects.get(id = id)
        single_product = Product_serializer(product).data
        return Response(single_product)  
    
    # def patch(self, request, id):
    #     product = Product.objects.filter(id = id)
    #     product.update(product_name = request.data['product_name'], product_code = request.data['product_code'], price = request.data['price'], rating = request.data['rating'],category_id = request.data[category_id])
    #     return Response("Data Updated")
    
    def patch(self, request, id):
        product = Product.objects.get(id = id)
        new_product = Product_serializer(product, data=request.data, partial = True)
        if new_product.is_valid():
            new_product.save()
            return Response("Data Updated")
        else:
            return Response(new_product.errors)    
        


    def delete(self, request, id):
        product = Product.objects.get(id = id)
        product.delete()
        return Response("Data Deleted")  
    

class CategoryView(APIView):

    def get(self, request):
        serializer_category = Category_serializer(Category.objects.all(), many=True) 
        return Response(serializer_category.data) 
    
    def post(self, request):
        new_category = Category_serializer(data=request.data)

        if new_category.is_valid():
            new_category.save()
            return Response("Data Saved")
        else:
            return Response(new_category.errors)

class CategoryViewById(APIView):
    def delete(self, request, id):
        category_delete = Category.objects.get(id = id)
        category_delete.delete()
        return Response("Data Deleted")            