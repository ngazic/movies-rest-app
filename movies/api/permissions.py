from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        print(request.user.is_authenticated)
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)


class IsReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print('has object permission')
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            print(request.user)
            print('request user =========')
            return obj.review_user == request.user #or request.user.is_staff
