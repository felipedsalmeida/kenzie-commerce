from django.urls import path
from .views import ListCreateOrder, RetrieveUpdateDestroyOrder, ListDeveliredOrder, ListPlacedOrder

urlpatterns = [path("orders/", ListCreateOrder.as_view()),
               path("orders/<int:orderId>/", RetrieveUpdateDestroyOrder.as_view()),
               path("orders/delivered/", ListDeveliredOrder.as_view()),
               path("orders/placed/", ListPlacedOrder.as_view())]

