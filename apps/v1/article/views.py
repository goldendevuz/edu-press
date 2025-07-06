import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import viewsets
from .serializers import PromoteUserSerializer


User = get_user_model()

from apps.v1.article.permissions import IsWriterOrReadOnly
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsWriterOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PromoteToWriterView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def normalize_uuid(self, uuid_string):
        """Convert UUID without dashes into proper UUID format."""
        if len(uuid_string) == 32:
            return str(uuid.UUID(uuid_string))
        return uuid_string

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='user_id',
                type=OpenApiTypes.UUID,
                location=OpenApiParameter.PATH,
                required=True,
                description='UUID of the user to promote',
                examples=[
                    OpenApiExample(
                        name="uuid_without_dashes",
                        value="2557107c9c9841a48f142a8d56ceb2ad",
                        summary="UUID without dashes",
                    ),
                    OpenApiExample(
                        name="uuid_with_dashes",
                        value="2557107c-9c98-41a4-8f14-2a8d56ceb2ad",
                        summary="UUID with dashes",
                    ),
                ]
            )
        ]
    )
    def post(self, request, user_id):
        try:
            user_id = self.normalize_uuid(str(user_id))
        except ValueError:
            return Response({'detail': 'Invalid UUID format.'}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, id=user_id)

        if user.user_roles == 'writer':
            return Response({'detail': 'User is already a writer.'}, status=status.HTTP_400_BAD_REQUEST)

        user.user_roles = 'writer'
        user.save()

        return Response(PromoteUserSerializer(user).data, status=status.HTTP_200_OK)