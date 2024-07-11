from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from texnomart.models import Product

# Create your views here.



class ProductListApi(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request):
        products = Product.objects.all()
        product_data = [
            {
                'id': product.id,
                'name' :product.name,
                'description' : product.description,
                'price' : product.price,
                'image' : product.image.url,
                'rating' : product.rating,
                'discount_price' : product.discount_priced,
                
            
            
            
            }
            for product in products
        ]

        return Response(product_data)