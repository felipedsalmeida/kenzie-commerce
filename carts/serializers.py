from rest_framework import serializers
from carts.models import Cart_Products
from carts.models import Cart_Products, Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "products"]
        depth = 1


class CartProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        return Cart_Products.objects.create(**validated_data)

    class Meta:
        model = Cart_Products
        fields = ["id", "cart_id", "product_id", "product", "amount"]
        read_only_fields = ["cart_id"]
        depth = 1
