from django.db import models
from apps.v1.shared.models import BaseModel
from .course import Course


class CourseFaq(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f'{self.course.title} – {self.question}'
