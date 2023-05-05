from django.urls import path
from .views import RetrieveCart, UpdateCart

urlpatterns = [
    path("carts/", RetrieveCart.as_view()),
    path("carts/products/", UpdateCart.as_view()),
]
