from rest_framework import permissions
from rest_framework.views import Request, View

from users.models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class OwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        if request.method in permissions.SAFE_METHODS and obj == request.user:
            return True

        elif request.user.is_superuser or obj == request.user:
            return True

        return False
