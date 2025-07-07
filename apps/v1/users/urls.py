from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CreateUserView, PromoteToInstructorView, UserViewSet, VerifyAPIView, GetNewVerification, \
    UpdateUserInformationView, ChangeUserPhotoView, LoginView, LoginRefreshView, \
    LogOutView, ResetPasswordView, PasswordGeneratorView, test_login

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', LoginRefreshView.as_view(), name='refresh'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('verify/', VerifyAPIView.as_view(), name='verify'),
    path('new-verify/', GetNewVerification.as_view(), name='new-verify'),
    path('update', UpdateUserInformationView.as_view(), name='update'),
    path('photo/', ChangeUserPhotoView.as_view()),
    path('reset-password/', ResetPasswordView.as_view()),
    path('test-login/', test_login, name='test-login'),
    path('generate-password/', PasswordGeneratorView.as_view(), name='generate-password'),
    path('promote-to-instructor/<uuid:user_id>/', PromoteToInstructorView.as_view(), name='promote-to-instructor'),
]

urlpatterns += router.urls
