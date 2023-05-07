from rest_framework import serializers
from carts.models import Cart_Products


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Products
        fields = ["id", "user", "products"]
        depth = 1


class CartProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Cart_Products.objects.create(**validated_data)

    class Meta:
        model = Cart_Products
        fields = ["id", "cart_id", "product_id", "amount"]
        depth = 1
