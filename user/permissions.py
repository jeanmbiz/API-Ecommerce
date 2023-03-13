from rest_framework import permissions


class UpdatePermission(permissions.BasePermission):
    def has_object_permission(self, request, vie, obj) -> bool:
        if request.user.is_superuser and request.user.is_authenticated:
            return True

        if request.user.is_authenticated and obj == request.user:
            return True

        return False
