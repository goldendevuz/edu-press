from django.db import models
from apps.v1.shared.models import BaseModel

class ArticleTag(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
