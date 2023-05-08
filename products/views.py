from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from products.models import Product
from products.permissions import IsAdminOrSeller
from products.serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSeller]

    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user)

    def get_queryset(self):
        main_queryset = Product.objects.all()
        id = self.request.query_params.get("id")
        name = self.request.query_params.get("name")
        category = self.request.query_params.get("category")
        page = self.request.query_params.get("page")

        if not bool(self.request.query_params):
            return main_queryset

        if id:
            queryset = main_queryset.filter(id__exact=id)
            return queryset
        if name:
            queryset = main_queryset.filter(name__icontains=name)
            return queryset
        if category:
            queryset = main_queryset.filter(category__icontains=category)
            return queryset
        if page:
            return main_queryset


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSeller]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
