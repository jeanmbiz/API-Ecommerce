from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=127, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    employee = models.BooleanField(default=False)
    costumer = models.BooleanField(default=False)
