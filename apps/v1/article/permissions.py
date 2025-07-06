from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsWriterOrReadOnly(BasePermission):
    """
    Allows full access only to users with user_roles='writer'.
    Read-only access is allowed to any authenticated user.
    """

    def has_permission(self, request, view):
        # Allow read-only access to any request
        if request.method in SAFE_METHODS:
            return True

        # Allow write access only to authenticated users with role 'writer'
        return (
            request.user
            and request.user.is_authenticated
            and getattr(request.user, 'user_roles', None) == 'writer'
        )

