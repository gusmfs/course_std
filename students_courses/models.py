import uuid
from django.db import models
from accounts.models import Account

from courses.models import Course

# Create your models here.
class StudentCourse(models.Model):
    class STUDENT_COURSE_STATUS(models.TextChoices):
        pending = 'pending'
        accepted = 'accepted'

    id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    status = models.CharField(max_length=20 ,choices=STUDENT_COURSE_STATUS, default=STUDENT_COURSE_STATUS.pending)
    student = models.ForeignKey(Account, related_name='students_courses', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='students_courses', on_delete=models.CASCADE)