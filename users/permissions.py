from rest_framework import permissions
from .models import User
from rest_framework.views import View
from users.models import USER_TYPE


class IsAdminOrUser(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        if request.user.type == USER_TYPE.ADMIN or obj == request.user:
            return True
