from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from students_courses.models import StudentCourse

class StudentsCourseSerializer(ModelSerializer):
    student_id = serializers.CharField(source='student.id', read_only=True)
    student_email = serializers.CharField(source='student.email' )
    student_username = serializers.CharField(source='student.username', read_only=True) 

    class Meta: 
        model = StudentCourse
        fields = ['id', 'student_id', 'student_username', 'student_email', 'status']
