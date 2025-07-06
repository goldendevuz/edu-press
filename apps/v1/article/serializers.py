from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, ArticleCategory, ArticleTag

User = get_user_model()

class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ['id', 'name']  # adjust fields

class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ['id', 'name']  # adjust fields

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'thumbnail', 'title', 'date', 'description', 'category', 'tags', 'author']

class PromoteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'user_roles']
        read_only_fields = ['id', 'username', 'user_roles']
