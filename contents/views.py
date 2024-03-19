from django.shortcuts import get_object_or_404, render

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView  , RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from contents.models import Content
from contents.serializers import ContentSerializer
from courses.models import Course
from exceptions import NotFoundException
from rest_framework.exceptions import NotFound
from permissions import AccountPermission, IsAdminOrOwner, IsStudentOfCourse, IsSuperUser, IsSuperuserOrParticipant
# Create your views here.
class CreateContentAPIView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AccountPermission]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    def perform_create(self, serializer):
        course = Course.objects.get(pk = self.kwargs.get('course_id'))
        if not course:
            raise NotFound({'detail' : 'course not found.'})
        serializer.save(course=course)

class RetrieveUpdateDestroyCourseAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [ AccountPermission , IsSuperuserOrParticipant]
    lookup_url_kwarg = 'content_id'
    def get_object(self):
        try:
            Course.objects.get(pk=self.kwargs['course_id'])
            content = Content.objects.get(pk=self.kwargs['content_id'])

        except Course.DoesNotExist:
            raise NotFound({'detail': 'course not found.'})
        except Content.DoesNotExist:
            raise NotFound({'detail': 'content not found.'})
        self.check_object_permissions(self.request, content)
        return content
