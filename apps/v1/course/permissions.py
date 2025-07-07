from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            (request.user and request.user.is_staff)
        )

class IsInstructorOrReadOnly(BasePermission):
    """
    Allows full access only to users with user_roles='instructor'.
    Read-only access is allowed to any user.
    """

    def has_permission(self, request, view):
        # Allow read-only access to any request
        if request.method in SAFE_METHODS:
            return True

        # Allow write access only to authenticated users with role 'instructor'
        return (
            request.user
            and request.user.is_authenticated
            and getattr(request.user, 'user_roles', None) == 'instructor'
        )