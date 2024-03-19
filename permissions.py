from django.views import View
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import permissions

from accounts.models import Account
from contents.models import Content


class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Account):
        return request.user.is_superuser or request.user == obj


class IsStudentOfCourse(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.method == "GET"

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user in obj.students.all()


class IsSuperUser(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Account):
        return request.user.is_superuser


# class IsSuperuserOrParticipant(permissions.BasePermission):
    # def has_permission(self, request: Request, view: View):
        # if request.user.is_superuser:
            # return True
        # return request.method in permissions.SAFE_METHODS
# 
    # def has_object_permission(self, request: Request, view: View, obj: Course):
        # return request.user.is_superuser or request.user in obj.students.all()


class IsSuperuserOrParticipant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Content):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user in obj.course.students.all()
            or request.user.is_superuser
        )

class AccountPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_superuser
    
