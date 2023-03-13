from rest_framework import permissions


class RegisterAddressPermission(permissions.BasePermission):
    def has_object_permission(self, request, vie, obj) -> bool:
        return request.user and request.user.is_authenticated
