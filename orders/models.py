from django.db import models
import uuid


class StatusChoices(models.TextChoices):
    DEFAULT = "Realizado"
    in_progress = "Em andamento"
    delivered = "Entregue"


class Orders(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.DEFAULT,
    )
    price = models.IntegerField()

    ordered_at = models.DateTimeField(auto_now_add=True)

    address = models.ForeignKey(
        "address.Address", on_delete=models.CASCADE, related_name="address"
    )

    cart = models.ForeignKey(
        "cart.Cart", on_delete=models.CASCADE, related_name="cart_orders"
    )
