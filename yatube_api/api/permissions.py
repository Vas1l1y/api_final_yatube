from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' or request.method == 'PATCH':
            return obj.author == request.user
        return Response(status=status.HTTP_403_FORBIDDEN)
