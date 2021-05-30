from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Checks whether the requesting user is also the owner of the existing object"""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


def OwnerCUD_AuthR(view, view_super):
    if view.action in ['create', 'update', 'partial_update', 'destroy']:
        view.permission_classes = [IsOwner]
    elif view.action in ['list']:
        view.permission_classes = [permissions.IsAuthenticated]
    return view_super.get_permissions()


def AdminCUD_AuthR(view, view_super):
    if view.action in ['create', 'update', 'partial_update', 'destroy']:
        view.permission_classes = [permissions.IsAdminUser]
    elif view.action in ['list']:
        view.permission_classes = [permissions.IsAuthenticated]
    return view_super.get_permissions()
