from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    def get_user(self, dict: Address) -> dict:
        return {
            "email": dict.user.email,
        }

    class Meta:

        model = Address

        fields = [
            "id",
            "zip_code",
            "street",
            "number",
            "city",
            "state",
            "user",
        ]

        depth = 1
