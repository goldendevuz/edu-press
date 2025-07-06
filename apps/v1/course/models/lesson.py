from django.db import models
from apps.v1.shared.models import BaseModel
from .course import Course


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    content = models.TextField(blank=True)

    def __str__(self):
        return f'{self.course.title} - {self.title}'

    class Meta:
        ordering = ['order']
