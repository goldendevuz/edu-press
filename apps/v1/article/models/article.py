from django.db import models
from django.contrib.auth import get_user_model
from apps.v1.shared.models import BaseModel
from .article_category import ArticleCategory
from .article_tag import ArticleTag

User = get_user_model()

class Article(BaseModel):
    thumbnail = models.ImageField(upload_to='articles/thumbnails/')
    title = models.CharField(max_length=255, unique=True)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    category = models.ManyToManyField(ArticleCategory, related_name='articles')
    tags = models.ManyToManyField(ArticleTag, related_name='articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title
