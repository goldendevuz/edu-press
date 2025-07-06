from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from config import API_V1_URL
from core.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('schema-viewer/', include('schema_viewer.urls')),

    # Spectacular schema and UI docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Include your app routes
    path(API_V1_URL+'user/', include('apps.v1.users.urls')),
    path(API_V1_URL+'api-auth/', include('rest_framework.urls')),  # Important for login/logout
    path(API_V1_URL+'articles/', include('apps.v1.article.urls')),
    path(API_V1_URL+'courses/', include('apps.v1.course.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)