from rest_framework import permissions
from rest_framework.views import View
from users.models import User, USER_TYPE
import ipdb


class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        if request.user.is_authenticated:
            if (
                request.user.type == USER_TYPE.ADMIN
                or request.user.type == USER_TYPE.SELLER
            ):
                return True
        elif request.method in permissions.SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            # ipdb.set_trace()
            if request.user.type == USER_TYPE.ADMIN or request.user.id == obj.seller_id:
                return True
        elif request.method in permissions.SAFE_METHODS:
            return True
