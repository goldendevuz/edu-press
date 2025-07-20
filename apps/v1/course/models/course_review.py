from django.db import models
from apps.v1.shared.models import BaseModel
from .student import Student
from .course import Course  # Make sure Course model is correctly imported

class CourseReview(BaseModel):
    STARS_CHOICES = [(i, f"{i} stars") for i in range(0, 6)]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    date = models.DateField()
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(choices=STARS_CHOICES, default=0)

    def __str__(self):
        return f'Review by {self.student.user.username} on {self.date} for {self.course.title}'

    class Meta:
        unique_together = ('student', 'course')
        verbose_name = "Course Review"
        verbose_name_plural = "Course Reviews"


