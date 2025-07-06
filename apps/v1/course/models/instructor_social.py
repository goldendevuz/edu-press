from django.db import models
from apps.v1.shared.models import BaseModel
from .instructor import Instructor
from .social import Social


class InstructorSocial(BaseModel):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='social_links')
    social = models.ForeignKey(Social, on_delete=models.CASCADE, related_name='instructor_links')

    def __str__(self):
        return f'{self.instructor.name} - {self.social.name}'

    class Meta:
        unique_together = ('instructor', 'social')  # Prevent duplicates
