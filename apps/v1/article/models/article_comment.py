from django.db import models
from django.contrib.auth import get_user_model
from apps.v1.shared.models import BaseModel
from .article import Article

User = get_user_model()

class ArticleComment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    replied_to = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )

    def __str__(self):
        return f"{self.user} - {self.text[:30]}"
