from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated
from carts.models import Cart_Products, Cart
from carts.serializers import CartProductSerializer, CartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import Product


class CartProductView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartProductSerializer

    def get_queryset(self):
        return Cart_Products.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        amount = serializer.validated_data["amount"]
        product = get_object_or_404(
            Product, pk=serializer.validated_data["product_id"]
        )

        if amount > product.stock:
            raise ValueError(
                f"Seller only has {product.stock} of {product.name} in stock."
            )

        already_in_cart = Cart_Products.objects.filter(
            product_id=serializer.validated_data["product_id"]
        ).first()

        if already_in_cart:
            already_in_cart.delete()

        serializer.save(
            product_id=serializer.validated_data["product_id"],
            cart_id=self.request.user.cart.id,
        )


class CartDetailView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Cart.objects.filter(id=self.kwargs.get('pk'))
        return Cart.objects.filter(user=self.request.user)
