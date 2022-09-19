from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return obj.author == request.user
        return request.method in permissions.SAFE_METHODS
