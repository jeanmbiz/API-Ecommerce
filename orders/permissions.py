from rest_framework.views import Request, View
from rest_framework import permissions


class IsAuthenticatedPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return request.user.is_authenticated and request.user == obj
