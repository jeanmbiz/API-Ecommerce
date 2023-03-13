from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import User


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser

        return token


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        if validated_data["employee"] or validated_data["costumer"]:
            return User.objects.create_user(**validated_data)
        elif not validated_data["employee"]:
            return User.objects.create_superuser(**validated_data)

    def update(self, instance, validated_data):

        setattr(instance, "employee", validated_data["employee"])
        instance.save()

        return instance

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "email",
            "password",
            "created_at",
            "employee",
            "costumer",
            "is_superuser",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "created_at": {"read_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This field must be unique.",
                    )
                ],
                "required": True,
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This field must be unique.",
                    )
                ],
                "required": True,
            },
        }
