from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer



class CategoryViewSet(viewsets.ViewSet):
    """Category ViewSet"""
    queryset = Category.objects.all()
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
