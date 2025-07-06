from django.db import models
from apps.v1.shared.models import BaseModel
from .student import Student


class CourseReview(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reviews')
    date = models.DateField()
    text = models.TextField()

    def __str__(self):
        return f'Review by {self.student.user.username} on {self.date}'
