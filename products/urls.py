from django.urls import path
from .views import ListCreateProduct

urlpatterns = [path("products/", ListCreateProduct.as_view())]
