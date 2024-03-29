from rest_framework import serializers
from orders.models import Order, Order_Products
from carts.models import Cart_Products
from products.serializers import ProductSerializer
from users.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True)
    order_products = serializers.SerializerMethodField()
    # seller = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data):
        products = [(cp.product, cp.amount) for cp in Cart_Products.objects.filter(cart_id = validated_data.get("buyer").id)]
        
        seller_dict = {}
        order = None
        
        for product, amount in products:            
            try:
                #if product.username in seller_dict:
                seller_dict[product.seller.username] += [product]
                    
            except:
                seller_dict[product.seller.username] = [product]
                order = Order.objects.create(**validated_data)

            Order_Products.objects.create(order = order, product = product, amount = amount)
            product.stock -= amount
            product.save()
        
        
        return order

    def get_order_products(self, order):
        order_products = Order_Products.objects.filter(order_id = order.id)
        order_list = []
        for op in order_products:
            #print(op.product.seller)
            order_list.append({"product_id": op.product.id,
                               "name":op.product.name, 
                               "category": op.product.category, 
                               "price": op.product.price, 
                               "seller": f"{op.product.seller.first_name} {op.product.seller.last_name}", 
                               "amount": op.amount})
        return order_list

    # def get_seller(self, order):
    #     seller = Order_Products.objects.filter(seller = order.product.seller)
    #     return order.status

    class Meta:
        model = Order
        fields = ["id", "buyer", "status", "created_at", "order_products"]
        
        # fields = ["id", "buyer_id", "status", "products", "created_at"]
        #read_only_fields = ["buyer", "products"]
        
