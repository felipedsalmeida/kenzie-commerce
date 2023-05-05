from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from products.models import Product
from products.serializers import ProductSerializer


class ListCreateProduct(CreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def perform_create(self, serializer):
    #     return serializer.save()
    ...
