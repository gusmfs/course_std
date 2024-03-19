from django.shortcuts import get_object_or_404, render

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView  , RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from accounts.models import Account
from accounts.serializers import AccountSerializer
from contents.models import Content
from contents.serializers import ContentSerializer
from courses.models import Course
from courses.serializers import CourseSerializer, CourseStudentSerializer
from permissions import AccountPermission, IsAdminOrOwner, IsStudentOfCourse, IsSuperUser, IsSuperuserOrParticipant

# Create your views here.


class ListCreateCourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AccountPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Course.objects.filter(students = self.request.user)
        return self.queryset.all()

class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AccountPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = 'course_id'
        


class UpdateCourseStudent(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseStudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AccountPermission]
    lookup_url_kwarg = 'course_id'



