from .models import Cart, ProductsInCart
from rest_framework import serializers
from products.models import Product
from user.models import User


class StringListField(serializers.ListField):
    id = serializers.CharField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()
    employee_email = serializers.CharField()


class CartSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    products = StringListField()
    value = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        cart_id = []
        total_price = 0
        products = []

        for item in validated_data["products"]:
            product = Product.objects.get(pk=item["id"])
            product_price = product.price * item["quantity"]
            product_stock = product.stock
            stock_result = product_stock - item["quantity"]
            setattr(product, "stock", stock_result)
            product.save()
            total_price += product_price
            employee = User.objects.get(pk=product.user.id)

            try:
                cart = Cart.objects.get(user_id=validated_data["user"].id)
            except Cart.DoesNotExist:
                cart = Cart.objects.create(
                    value=product_price, user_id=validated_data["user"].id
                )

            cart_id.append(cart.id)

            ProductsInCart.objects.create(
                quantity=item["quantity"], product=product, cart=cart
            )
            products.append(
                {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "quantity": item["quantity"],
                    "employee_email": employee.email,
                }
            )

        return {"id": cart_id[0], "value": total_price, "products": products}
