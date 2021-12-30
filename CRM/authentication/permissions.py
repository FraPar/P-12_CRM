from rest_framework import permissions
from .models import User

supervisor = "SUPERVISOR"
sales = "SALES"
support = "SUPPORT"

class IsSupervisor(permissions.BasePermission):

    queryset = User.objects.all()

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == supervisor:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.role == supervisor:
            return True

        return False


class IsSupport(permissions.BasePermission):

    queryset = User.objects.all()

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == support:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.role == supervisor or request.user.role == support:
            return True

        return False
        

class IsSales (permissions.BasePermission):

    queryset = User.objects.all()

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == sales:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.role == supervisor or request.user.role == sales:
            return True

        return False


class IsClientSales (permissions.BasePermission):

    pass


class IsSupportOnEvent (permissions.BasePermission):

    pass

