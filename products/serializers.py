from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    seller = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "price",
            "stock",
            "seller",
        ]

    def get_seller(self, obj):
        return f"{obj.seller.first_name} {obj.seller.last_name}"
