from django.db import models
from apps.v1.shared.models import BaseModel
from .course_category import CourseCategory
from .instructor import Instructor
from .curriculum import Curriculum


class Course(BaseModel):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)

    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    curriculum = models.ForeignKey(Curriculum, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    thumbnail = models.ImageField(upload_to='course_thumbnails/')
    weeks_count = models.PositiveIntegerField()
    common_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    description = models.TextField()
    instructor_summary = models.TextField()

    def __str__(self):
        return self.title
