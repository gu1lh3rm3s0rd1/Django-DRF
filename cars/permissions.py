from rest_framework import permissions

# classe de permissão para o dono do carro
class CarOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # get
        if view.action == 'list':
            view.queryset = view.queryset.filter(owner=request.user)
            return True
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user