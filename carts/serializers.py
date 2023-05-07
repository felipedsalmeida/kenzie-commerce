from itertools import product
from rest_framework import serializers
from carts.models import Cart_Products, Cart
from products.serializers import ProductSerializer
from products.models import Product
import ipdb
# from products.serializers import ProductSerializer
# from users.serializers import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    # user = UserSerializer()

    class Meta:
        model = Cart
        # fields = ["id", "user", "products"]
        fields = ["id", "products"]
        depth = 1


class CartProductSerializer(serializers.ModelSerializer):
    # cart_id = serializers.IntegerField()
    product_id = serializers.IntegerField()

    def create(self, validated_data):
        return Cart_Products.objects.create(**validated_data)
        # ipdb.set_trace()
        # print(Product.objects.get(id=self.validated_data["product"]))
        # return Product.objects.get(id=self.validated_data["product"])

    class Meta:
        model = Cart_Products
        fields = ["id", "cart_id", "product_id", "amount"]
        read_only_fields = ['cart_id']
        depth = 1
