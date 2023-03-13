from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=127)
    number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=127)

    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="address"
    )
