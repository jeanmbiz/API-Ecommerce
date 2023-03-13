from rest_framework import permissions


class CreateProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        return (
            request.user.is_superuser or request.user.employee
        ) and request.user.is_authenticated
