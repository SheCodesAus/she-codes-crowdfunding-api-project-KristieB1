from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permisssion(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
                return True
        return object.owner == request.user