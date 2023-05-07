from django.urls import path
from .views import ListCreateOrder

urlpatterns = [path("orders/", ListCreateOrder.as_view())]
