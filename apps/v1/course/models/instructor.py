from django.db import models
from django.contrib.auth import get_user_model
from apps.v1.shared.models import BaseModel

User = get_user_model()

class Instructor(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
