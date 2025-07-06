from django.db import models
from apps.v1.shared.models import BaseModel
from .lesson import Lesson


class Quiz(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    instructions = models.TextField(blank=True)
    time_limit = models.PositiveIntegerField(help_text='Time limit in minutes', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Quiz: {self.title} ({self.lesson.title})'
