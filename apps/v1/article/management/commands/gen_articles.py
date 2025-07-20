import random
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.utils.text import slugify
from faker import Faker
from apps.v1.article.models import Article
from apps.v1.article.models import ArticleCategory, ArticleTag
from django.contrib.auth import get_user_model

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = "Generate 6 sample articles for Udemy clone"

    def handle(self, *args, **kwargs):
        # Ensure at least 1 author exists
        authors = User.objects.all()
        if not authors.exists():
            self.stdout.write(self.style.ERROR("No users found. Create at least one user first."))
            return

        # Dummy categories and tags fallback
        categories = list(ArticleCategory.objects.all())
        tags = list(ArticleTag.objects.all())

        titles = [
            "How to Master Python for Web Development",
            "Top 10 Tips for Learning Online Effectively",
            "The Future of EdTech Platforms",
            "Why Soft Skills Matter in Tech Careers",
            "Building a Portfolio That Gets You Hired",
            "Understanding the Basics of Machine Learning"
        ]

        created = 0

        for title in titles:
            if Article.objects.filter(title=title).exists():
                continue

            author = random.choice(authors)
            description = fake.paragraph(nb_sentences=7)
            thumbnail = ContentFile(fake.image(), name=f"{slugify(title)}.jpg")

            article = Article.objects.create(
                title=title,
                description=description,
                thumbnail=thumbnail,
                author=author
            )

            # Randomly add categories and tags
            if categories:
                article.category.set(random.sample(categories, min(2, len(categories))))
            if tags:
                article.tags.set(random.sample(tags, min(3, len(tags))))

            created += 1

        self.stdout.write(self.style.SUCCESS(f"{created} articles created successfully."))
