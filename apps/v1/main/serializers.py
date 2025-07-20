from rest_framework import serializers
from apps.v1.main.models.faq import Faq

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'question', 'answer', 'created']