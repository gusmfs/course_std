from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('courses/<course_id>/contents/', views.CreateContentAPIView.as_view()),
    path('courses/<course_id>/contents/<content_id>/', views.RetrieveUpdateDestroyCourseAPIView.as_view())
]