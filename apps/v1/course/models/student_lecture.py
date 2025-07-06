from django.db import models
from apps.v1.shared.models import BaseModel
from .student import Student
from .course_lecture import CourseLecture


class StudentLecture(BaseModel):
    class Status(models.TextChoices):
        NOT_STARTED = 'not_started', 'Not Started'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='lecture_progress')
    lecture = models.ForeignKey(CourseLecture, on_delete=models.CASCADE, related_name='student_progress')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NOT_STARTED)

    def __str__(self):
        return f'{self.student.user.username} - {self.lecture.name} ({self.status})'

    class Meta:
        unique_together = ('student', 'lecture')  # prevent duplicates
