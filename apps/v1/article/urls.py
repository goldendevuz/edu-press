from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet
from django.urls import path
from .views import PromoteToWriterView

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='article')

urlpatterns = [
    path('promote-to-writer/<uuid:user_id>/', PromoteToWriterView.as_view(), name='promote-to-writer'),
]


urlpatterns += router.urls
