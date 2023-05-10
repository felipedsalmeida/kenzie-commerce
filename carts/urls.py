from django.urls import path
from .views import CartDetailView, CartProductView

urlpatterns = [
    path("carts/<int:pk>/", CartDetailView.as_view()),
    path("carts/products/", CartProductView.as_view()),
]