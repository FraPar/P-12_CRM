from rest_framework import permissions
from .models import User
from client.models import Client

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

    userset = User.objects.all()
    clientset = Client.objects.all()

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == sales:
            return True
        return False

    def has_object_permission(self, request, view, post):
        if request.user.is_superuser:
            return True

        if request.user.role == supervisor or request.user.role == sales:
            try :
                print("There IS SALES_CONTACT (CLIENT|CONTRACT)")
                if request.user == post.sales_contact:
                    print("This IS the owner")
                    return True
                #if request.user.id == post.author:
                print("This is NOT the owner")
                print(request.user)
                print(post.sales_contact)
                return False
            except AttributeError:
                print("There is NO SALES_CONTACT (EVENT)")
                client_id = post.client.id
                clientset = Client.objects.filter(id=client_id)
                if request.user == clientset[0].sales_contact:
                    print("This IS the owner")
                    return True
                print("This is NOT the owner")
                return False
        return False

class IsSupportOnEvent (permissions.BasePermission):

    pass

