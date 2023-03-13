from django.db import models
import uuid


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    value = models.IntegerField()
    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        related_name="cart",
    )
    products = models.ManyToManyField(
        "products.Product",
        through="cart.ProductsInCart",
        related_name="products",
    )


class ProductsInCart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    quantity = models.IntegerField()

    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="products_carts"
    )
    cart = models.ForeignKey(
        "cart.Cart", on_delete=models.CASCADE, related_name="cart_products"
    )
