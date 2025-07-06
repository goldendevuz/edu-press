from django.db import models
from apps.v1.shared.models import BaseModel
from .course import Course


class CourseSection(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.course.title} - {self.name}'
