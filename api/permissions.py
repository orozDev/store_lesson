from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from pprint import pprint

from core.models import Product


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        product = get_object_or_404(Product, id=view.kwargs['id'])

        return product.user == request.user or request.user.is_superuser


class IsOwnerForProduct(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.product.user or request.user.is_superuser


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):

        return request.user.is_superuser


class IsSuperAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        return bool(
            request.method in SAFE_METHODS or
            request.user.is_superuser
        )