
from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """ Проверяем является ли пользователь автором. """

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False
