from django.db import models
from apps.v1.shared.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Student(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'Student: {self.user.get_full_name() or self.user.username}'
