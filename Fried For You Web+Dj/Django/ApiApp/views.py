from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    #查詢所有產品,按name排序
    serializer_class = ProductSerializer
    #指定序列化類別