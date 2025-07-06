from django.db import models
from apps.v1.shared.models import BaseModel

class Instructor(BaseModel):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='instructors/', blank=True, null=True)

    def __str__(self):
        return self.name
