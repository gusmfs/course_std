from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
#from courses.models import Course

# Create your models here.
class Account(AbstractUser):
    

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)

    #my_courses = models.ManyToManyField(Course, related_name='students', through='StudentCourse')

    def __str__(self):
        return self.username