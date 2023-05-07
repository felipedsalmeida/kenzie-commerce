from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from orders.models import Order
from orders.serializers import OrderSerializer


class ListCreateOrder(CreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def perform_create(self, serializer):
    #     return serializer.save()
    def perform_create(self, serializer):
        return serializer.save(buyer=self.request.user)
    ...
