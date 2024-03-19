from rest_framework.serializers import ModelSerializer, ValidationError
from accounts.models import Account

from courses.models import Course
from students_courses.serializers import StudentsCourseSerializer


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "status": {"read_only": True},
            "contents": {"read_only": True},
            "students_courses": {"read_only": True},
            
        }


class CourseStudentSerializer(ModelSerializer):
    students_courses = StudentsCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        extra_kwargs = {
            "name" : {'read_only': True},
            
        }
    def update(self, instance, validated_data):
        list = []
        list_not_found = []
        
        for student in validated_data["students_courses"]:
            email = student["student"]["email"]
            account = Account.objects.filter(email=email).first()
            if account:
                list.append(account)
            else:
                list_not_found.append(email)
        if list_not_found:
            message = ', '.join(list_not_found)
            raise ValidationError(
                {
                    "detail": f"No active accounts was found: {message}."
                }
            )
        
        instance.students.add(*list)
        return instance