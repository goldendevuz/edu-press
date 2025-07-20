import random
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from faker import Faker
from apps.v1.course.models import Course, CourseCategory, Instructor, Curriculum

fake = Faker()

class Command(BaseCommand):
    help = "Generate 6 demo courses"

    def handle(self, *args, **kwargs):
        categories = list(CourseCategory.objects.all())
        instructors = list(Instructor.objects.all())
        curricula = list(Curriculum.objects.all())

        if not categories or not instructors:
            self.stdout.write(self.style.ERROR("Please create at least 1 CourseCategory and 1 Instructor first."))
            return

        titles = [
            "Python for Absolute Beginners",
            "Fullstack Web Development Bootcamp",
            "Mastering Data Structures & Algorithms",
            "Advanced Django and REST API",
            "UI/UX Design Fundamentals",
            "Machine Learning with Real Projects"
        ]

        for title in titles:
            if Course.objects.filter(title=title).exists():
                continue

            course = Course.objects.create(
                title=title,
                is_featured=random.choice([True, False]),
                category=random.choice(categories),
                instructor=random.choice(instructors),
                curriculum=random.choice(curricula) if curricula else None,
                thumbnail=ContentFile(fake.image(), name=f"{title.lower().replace(' ', '_')}.jpg"),
                weeks_count=random.randint(4, 12),
                common_price=random.uniform(100.0, 300.0),
                current_price=random.uniform(50.0, 150.0),
                level=random.choice(["beginner", "intermediate", "advanced"]),
                description=fake.paragraph(nb_sentences=10),
                instructor_summary=fake.paragraph(nb_sentences=5)
            )

        self.stdout.write(self.style.SUCCESS("✅ 6 demo courses created successfully."))
