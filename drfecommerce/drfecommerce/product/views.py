from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response  import Response
from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CatergoryView(viewsets.ViewSet):
    """a view set for viewing all categories"""

    queryset = Category.objects.all()

def list (self, request):
    """list all categories"""
    serializer = CategorySerializer(self.queryset, many=True)
    return Response(serializer.data)