import os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from apps.v1.course.models import CourseCategory  # Adjust the path if needed


class Command(BaseCommand):
    help = 'Create or update CourseCategory objects with icons'

    def handle(self, *args, **options):
        icon_folder = os.path.join(settings.MEDIA_ROOT, 'category_icons')

        category_data = {
            'Art & Design': 'art_and_design.png',
            'Development': 'development.png',
            'Communication': 'communication.png',
            'Videography': 'videography.png',
            'Photography': 'photography.png',
            'Marketing': 'marketing.png',
            'Content Writing': 'content_writing.png',
            'Finance': 'finance.png',
            'Science': 'science.png',
            'Network': 'network.png',
        }

        for name, filename in category_data.items():
            file_path = os.path.join(icon_folder, filename)

            if not os.path.exists(file_path):
                self.stdout.write(self.style.WARNING(f'File not found: {file_path}'))
                continue

            # Create or update the category
            category, created = CourseCategory.objects.get_or_create(name=name, is_top=True)
            
            # Update icon only if newly created or different filename
            if created or not category.icon.name.endswith(filename):
                with open(file_path, 'rb') as f:
                    category.icon.save(filename, File(f), save=True)

            self.stdout.write(
                self.style.SUCCESS(
                    f'{"Created" if created else "Updated"} category: {name}'
                )
            )
