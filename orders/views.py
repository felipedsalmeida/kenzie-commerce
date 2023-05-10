from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from orders.models import Order, Order_Products
from orders.serializers import OrderSerializer
from users.models import USER_TYPE
from rest_framework_simplejwt.authentication import JWTAuthentication


class ListCreateOrder(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminOrReadOnly]
    
    serializer_class = OrderSerializer

    # def perform_create(self, serializer):
    #     return serializer.save()

    def get_queryset(self):
        queryset = Order.objects.all()
        user = self.request.user
        print(queryset[0].products)
        if user.type == USER_TYPE.ADMIN:  
            return queryset

        if user.type == USER_TYPE.SELLER:
            return queryset.filter(buyer = 99)
            #return queryset #Descobrir uma foram de acessar o seller atraves do product

        if user.type == USER_TYPE.CUSTOMER: 
            return queryset.filter(buyer=user)        

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

class RetrieveUpdateDestroyOrder(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = "orderId"

class ListDeveliredOrder (ListAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = OrderSerializer
    
    def get_queryset(self):
        queryset = Order.objects.filter(status="Delivered")
        user = self.request.user

        if user.type == USER_TYPE.ADMIN:  
            return queryset

        if user.type == USER_TYPE.SELLER:
            return queryset.filter(products__seller__type = user.type)
            # return queryset.filter(status="Delivered", order_product = user)
            # return queryset #Descobrir uma foram de acessar o seller atraves do product

        if user.type == USER_TYPE.CUSTOMER: 
            return queryset.filter(buyer=user) 