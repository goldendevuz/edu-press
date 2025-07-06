from django.db import models
from apps.v1.shared.models import BaseModel


class Curriculum(BaseModel):
    description = models.TextField()

    def __str__(self):
        return f'Curriculum #{self.id}'
