from django.core.management.base import BaseCommand
from django.utils.timezone import now
from apps.v1.course.models import CourseReview, Course, Student
import random

class Command(BaseCommand):
    help = "Generate sample course reviews"

    def handle(self, *args, **options):
        students = Student.objects.all()
        courses = Course.objects.all()
        texts = [
            "Amazing course!",
            "Pretty good, I liked it.",
            "Decent but needs improvements.",
            "Well structured and easy to follow.",
            "Too basic for me.",
        ]

        created_count = 0

        for course in courses:
            for student in random.sample(list(students), min(5, len(students))):
                if not CourseReview.objects.filter(student=student, course=course).exists():
                    CourseReview.objects.create(
                        student=student,
                        course=course,
                        date=now().date(),
                        text=random.choice(texts),
                    )
                    created_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {created_count} sample reviews."))
