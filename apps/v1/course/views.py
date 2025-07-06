from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.v1.course.permissions import IsAdminOrReadOnly
from .models import (
    ContactUs, CourseCategory, CourseFaq, CourseLecture, CourseReview, CourseSection, Course, Curriculum, Faq, Feedback, InstructorSocial, Instructor, 
    Lesson, Quiz, Social, StudentLecture, Student
)
from .serializers import (
    ContactUsSerializer, CourseCategorySerializer, CourseFaqSerializer, CourseLectureSerializer, CourseReviewSerializer, CourseSectionSerializer, 
    CourseSerializer, CurriculumSerializer, FaqSerializer, FeedbackSerializer, InstructorSocialSerializer, InstructorSerializer, LessonSerializer,
    QuizSerializer, SocialSerializer, StudentLectureSerializer, StudentSerializer
)


class ContactUsCreateView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [AllowAny]

    def get_client_ip(self):
        x_forwarded = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded:
            return x_forwarded.split(',')[0]
        return self.request.META.get('REMOTE_ADDR')

    def perform_create(self, serializer):
        serializer.save(ip_address=self.get_client_ip())

class CourseCategoryViewSet(viewsets.ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = [MultiPartParser]


class CourseFaqViewSet(viewsets.ModelViewSet):
    queryset = CourseFaq.objects.all()
    serializer_class = CourseFaqSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_id = self.request.query_params.get('course')
        if course_id:
            return CourseFaq.objects.filter(course_id=course_id)
        return super().get_queryset()

class CourseLectureViewSet(viewsets.ModelViewSet):
    queryset = CourseLecture.objects.all()
    serializer_class = CourseLectureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        section_id = self.request.query_params.get('section')
        if section_id:
            return CourseLecture.objects.filter(course_section_id=section_id)
        return super().get_queryset()
    
class CourseReviewViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        student_id = self.request.query_params.get('student')
        if student_id:
            return CourseReview.objects.filter(student_id=student_id)
        return super().get_queryset()
    
class CourseSectionViewSet(viewsets.ModelViewSet):
    queryset = CourseSection.objects.all()
    serializer_class = CourseSectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_id = self.request.query_params.get('course')
        if course_id:
            return CourseSection.objects.filter(course_id=course_id)
        return super().get_queryset()
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        category = self.request.query_params.get('category')
        instructor = self.request.query_params.get('instructor')
        is_featured = self.request.query_params.get('featured')

        queryset = Course.objects.all()

        if category:
            queryset = queryset.filter(category_id=category)
        if instructor:
            queryset = queryset.filter(instructor_id=instructor)
        if is_featured:
            queryset = queryset.filter(is_featured=is_featured.lower() == 'true')

        return queryset
    
class CurriculumViewSet(viewsets.ModelViewSet):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class InstructorSocialViewSet(viewsets.ModelViewSet):
    queryset = InstructorSocial.objects.all()
    serializer_class = InstructorSocialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        instructor_id = self.request.query_params.get('instructor')
        if instructor_id:
            return InstructorSocial.objects.filter(instructor_id=instructor_id)
        return super().get_queryset()

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_id = self.request.query_params.get('course')
        if course_id:
            return Lesson.objects.filter(course_id=course_id).order_by('order')
        return super().get_queryset()
    
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        lesson_id = self.request.query_params.get('lesson')
        if lesson_id:
            return Quiz.objects.filter(lesson_id=lesson_id)
        return super().get_queryset()

class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class StudentLectureViewSet(viewsets.ModelViewSet):
    queryset = StudentLecture.objects.all()
    serializer_class = StudentLectureSerializer

    def get_queryset(self):
        student_id = self.request.query_params.get('student')
        lecture_id = self.request.query_params.get('lecture')
        qs = StudentLecture.objects.all()

        if student_id:
            qs = qs.filter(student_id=student_id)
        if lecture_id:
            qs = qs.filter(lecture_id=lecture_id)
        return qs

    def perform_create(self, serializer):
        # Automatically assign student if using self.request.user -> .student
        serializer.save()

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)