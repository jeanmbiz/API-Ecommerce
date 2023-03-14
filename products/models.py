from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    category = models.CharField(max_length=127)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    product_image = models.ImageField(null=True)

    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="products"
    )
