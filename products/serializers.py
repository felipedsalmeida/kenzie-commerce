from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product
        fields = ["id", "seller", "category", "name", "price", "stock"]
        # depth = 1 se for mostrar o orders
