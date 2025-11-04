from rest_framework.permissions import BasePermission


# placeholder
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return True
