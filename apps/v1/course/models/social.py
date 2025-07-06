from django.db import models
from apps.v1.shared.models import BaseModel


class Social(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='social_icons/', blank=True, null=True)
    url = models.URLField(help_text="Base URL or homepage of the platform (e.g. https://twitter.com/)")

    def __str__(self):
        return self.name
