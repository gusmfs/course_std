from django.db import models
import uuid

from accounts.models import Account
# Create your models here.
class Course(models.Model):
    class CourseStatus(models.TextChoices):
        not_started = 'not started' 
        in_progress = 'in progress'  
        finished = 'finished'

    class Meta:
        ordering = ['id']

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    status = models.CharField(max_length=11, choices=CourseStatus.choices, default=CourseStatus.not_started)
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(Account, related_name='my_courses', through='students_courses.StudentCourse')

    instructor = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='courses', null=True , default=None)

    def __str__(self):
        return self.name
