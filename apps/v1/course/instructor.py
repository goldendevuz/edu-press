from django.db import models
from apps.v1.shared.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Instructor(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructors')
    name = models.CharField(max_length=100)
    profile_url = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
