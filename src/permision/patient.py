from rest_framework.permissions import BasePermission, SAFE_METHODS

class AuthorAllStaffAllButEditOrReadOnly(BasePermission):
    edit_methods = ("PUT", "PATCH")

    message = 'permission denied, you\'re not the owner'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

    # def has_permission(self, request, view):
    #     if request.user.is_authenticated:
    #         return True
    #
    # def has_object_permission(self, request, view, obj):
    #     # if request.user.is_superuser:
    #     #     return True
    #     #
    #     # if request.method in permissions.SAFE_METHODS:
    #     #     return True
    #
    #     if obj.creator == request.user:
    #         print(f'obj.creator is = {obj.creator}')
    #         print(f'request.user is = {request.user}')
    #         return True
    #
    #     # if request.user.is_staff and request.method not in self.edit_methods:
    #     #     return True
    #
    #     return False
