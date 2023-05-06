from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated
from carts.models import Cart_Products, Cart
from carts.serializers import CartProductSerializer, CartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class UpdateCart(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartProductSerializer

    def get_queryset(self):
        return Cart_Products.objects.filter(user=self.request.user)

    def perform_create(self, serializer):

        check_for_product = Cart_Products.objects.filter(
            product_id=serializer.validated_data["product_id"]
        ).first()

        if check_for_product:
            check_for_product.amount = serializer.validated_data["amount"]
            return check_for_product.save()

        serializer.save(
            product_id=serializer.validated_data["product_id"],
            cart_id=self.request.user.cart["id"],
        )


class RetrieveCart(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
