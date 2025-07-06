from django.db import models
from apps.v1.shared.models import BaseModel


class CourseCategory(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='course_category_icons/', unique=True)
    is_top = models.BooleanField(default=False)

    def __str__(self):
        return self.name
