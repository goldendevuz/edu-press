from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ContactUsCreateView, CourseCategoryViewSet, CourseFaqViewSet, CourseLectureViewSet, CourseReviewViewSet, CourseSectionViewSet, CourseViewSet, 
    CurriculumViewSet, FeedbackViewSet, InstructorSocialViewSet, InstructorViewSet, LessonViewSet, QuizViewSet, SocialViewSet, 
    StudentLectureViewSet, StudentViewSet
)


router = DefaultRouter()
router.register(r'categories', CourseCategoryViewSet, basename='course-category')
router.register(r'curriculums', CurriculumViewSet, basename='curriculum')
router.register(r'faqs', CourseFaqViewSet, basename='course-faq')
router.register(r'lectures', CourseLectureViewSet, basename='course-lecture')
router.register(r'reviews', CourseReviewViewSet, basename='course-review')
router.register(r'sections', CourseSectionViewSet, basename='course-section')
router.register(r'feedbacks', FeedbackViewSet, basename='feedback')
router.register(r'instructor-socials', InstructorSocialViewSet, basename='instructor-social')
router.register(r'instructors', InstructorViewSet, basename='instructor')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'socials', SocialViewSet, basename='social')
router.register(r'student-lectures', StudentLectureViewSet, basename='student-lecture')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'', CourseViewSet, basename='course')

urlpatterns = [
    path('contact-us/', ContactUsCreateView.as_view(), name='contact-us'),
]

urlpatterns += router.urls