from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    class Meta:
        model = Order
        fields = ["id", "buyer", "status", "products", "created_at"]
        # fields = ["id", "buyer_id", "status", "products", "created_at"]
        depth = 1
