from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated
from carts.models import Cart_Products, Cart
from carts.serializers import CartProductSerializer, CartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from products.models import Product


class UpdateCart(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartProductSerializer

    def get_queryset(self):
        return Cart_Products.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        product = get_object_or_404(
            Product, id=serializer.validated_data["product_id"]
        )

        if serializer.validated_data["amount"] > product.stock:
            raise ValueError(
                f"Seller only has {product.stock} of {product.name} in stock."
            )

        already_in_cart = Cart_Products.objects.filter(
            product_id=serializer.validated_data["product_id"],
            cart_id=self.request.user.cart.id,
        ).first()

        if already_in_cart:
            already_in_cart.amount = serializer.validated_data["amount"]
            return already_in_cart.save()

        serializer.save(
            product_id=serializer.validated_data["product_id"],
            cart_id=self.request.user.cart.id,
        )


class RetrieveCart(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        user = User.objects.get(id=self.kwargs.get("pk"))
        return Cart.objects.get(user=user)
