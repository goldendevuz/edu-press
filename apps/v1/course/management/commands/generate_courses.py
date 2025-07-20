import random
from django.core.management.base import BaseCommand
from faker import Faker
from apps.v1.course.models import Course, CourseCategory, Instructor, Curriculum

fake = Faker()


class Command(BaseCommand):
    help = "Generate 10 fake course records"

    def handle(self, *args, **kwargs):
        if Course.objects.count() >= 10:
            self.stdout.write(self.style.WARNING("10 or more courses already exist. Aborting."))
            return

        categories = list(CourseCategory.objects.all())
        instructors = list(Instructor.objects.all())
        curriculums = list(Curriculum.objects.all())

        if not categories or not instructors:
            self.stdout.write(self.style.ERROR("Make sure you have categories and instructors first."))
            return

        for _ in range(10):
            course = Course.objects.create(
                title=fake.sentence(nb_words=4),
                is_featured=random.choice([True, False]),
                category=random.choice(categories),
                instructor=random.choice(instructors),
                curriculum=random.choice(curriculums) if curriculums else None,
                thumbnail="course_thumbnails/sample.jpg",  # Assumes a sample file exists
                weeks_count=random.randint(4, 12),
                common_price=round(random.uniform(100, 300), 2),
                current_price=round(random.uniform(50, 200), 2),
                level=random.choice(["beginner", "intermediate", "advanced"]),
                description=fake.paragraph(nb_sentences=5),
                instructor_summary=fake.paragraph(nb_sentences=3)
            )
            self.stdout.write(self.style.SUCCESS(f"✔ Created: {course.title}"))

        self.stdout.write(self.style.SUCCESS("🎉 Successfully generated 10 fake courses."))
