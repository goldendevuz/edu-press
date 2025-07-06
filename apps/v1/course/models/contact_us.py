from django.db import models
from apps.v1.shared.models import BaseModel


class ContactUs(BaseModel):
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    remember_me = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['ip_address', 'text'], name='unique_ip_text')
        ]

    def __str__(self):
        return f'Message from {self.name} ({self.email})'
