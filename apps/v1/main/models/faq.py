from django.db import models
from apps.v1.shared.models import BaseModel


class Faq(BaseModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
