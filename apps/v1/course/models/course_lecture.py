from django.db import models
from apps.v1.shared.models import BaseModel
from .course_section import CourseSection


class CourseLecture(BaseModel):
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE, related_name='lectures')
    name = models.CharField(max_length=255)
    has_preview = models.BooleanField(default=False)
    duration = models.DurationField(help_text="Duration of the lecture (HH:MM:SS)")

    def __str__(self):
        return f'{self.course_section.name} - {self.name}'
