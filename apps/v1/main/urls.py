from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    FaqViewSet
)


router = DefaultRouter()
router.register(r'faqs', FaqViewSet, basename='faq')

urlpatterns = router.urls