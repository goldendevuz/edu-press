from rest_framework import serializers

from .models import (
    ContactUs, CourseCategory, CourseFaq, CourseLecture, CourseReview, CourseSection, Course, Curriculum, Feedback, InstructorSocial, Instructor, 
    Lesson, Quiz, Social, StudentLecture, Student
)


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'text', 'remember_me', 'ip_address', 'created']
        read_only_fields = ['ip_address', 'created']

    def validate(self, attrs):
        request = self.context.get('request')
        ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        text = attrs.get('text')

        if ContactUs.objects.filter(ip_address=ip, text=text).exists():
            raise serializers.ValidationError("You have already submitted this message.")

        return attrs

class CourseCategorySerializer(serializers.ModelSerializer):
    is_top = serializers.BooleanField(default=False)  # explicitly tell DRF it's false

    class Meta:
        model = CourseCategory
        fields = ['id', 'name', 'icon', 'is_top', 'created']

class CourseFaqSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = CourseFaq
        fields = [
            'id',
            'course',
            'course_title',  # optional display
            'question',
            'answer',
            'created',
        ]
        
class CourseLectureSerializer(serializers.ModelSerializer):
    course_section_name = serializers.CharField(source='course_section.name', read_only=True)
    

    class Meta:
        model = CourseLecture
        fields = [
            'id',
            'course_section',
            'course_section_name',  # Optional, for display
            'name',
            'has_preview',
            'duration',
            'created',
        ]
        
class CourseReviewSerializer(serializers.ModelSerializer):
    student = serializers.UUIDField(read_only=True)
    student_username = serializers.CharField(source='student.user.username', read_only=True)
    course_name = serializers.CharField(source='course.title', read_only=True)
    date = serializers.DateField(read_only=True)  # <-- auto-filled

    class Meta:
        model = CourseReview
        fields = [
            'id',
            'student',
            'student_username',
            'course',
            'course_name',
            'date',
            'text',
            'stars',
            'created',
        ]
        
class CourseSectionSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    

    class Meta:
        model = CourseSection
        fields = [
            'id',
            'course',
            'course_title',  # optional for display
            'name',
            'created',
        ]
        
class CourseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    instructor_name = serializers.CharField(source='instructor.user.username', read_only=True)
    curriculum_name = serializers.CharField(source='curriculum.name', read_only=True, default=None)
    level_display = serializers.CharField(source='get_level_display', read_only=True)
    is_featured = serializers.BooleanField(default=False)  # explicitly tell DRF it's false
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'is_featured',
            'category',
            'category_name',
            'instructor',
            'instructor_name',
            'curriculum',
            'curriculum_name',
            'thumbnail',
            'weeks_count',
            'common_price',
            'current_price',
            'level',
            'level_display',
            'description',
            'instructor_summary',
            'avg_rating',
            'created',
        ]

class CurriculumSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Curriculum
        fields = ['id', 'description', 'created']
        
class FeedbackSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'username', 'text', 'created']
        read_only_fields = ['user']  # Auto-assign user in the view
        

class InstructorSocialSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='instructor.name', read_only=True)
    social_name = serializers.CharField(source='social.name', read_only=True)
    

    class Meta:
        model = InstructorSocial
        fields = [
            'id',
            'instructor',
            'instructor_name',
            'social',
            'social_name',
            'created',
        ]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=InstructorSocial.objects.all(),
                fields=['instructor', 'social'],
                message="This instructor already has this social linked."
            )
        ]

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'user', 'name', 'created']
        
class LessonSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    

    class Meta:
        model = Lesson
        fields = [
            'id',
            'course',
            'course_title',
            'title',
            'video_url',
            'order',
            'content',
            'created',
        ]
        
class QuizSerializer(serializers.ModelSerializer):
    lesson_title = serializers.CharField(source='lesson.title', read_only=True)
    

    class Meta:
        model = Quiz
        fields = [
            'id',
            'lesson',
            'lesson_title',
            'title',
            'instructions',
            'time_limit',
            'is_active',
            'created',
        ]

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id', 'name', 'icon', 'url', 'created']

class StudentLectureSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(source='student.user.username', read_only=True)
    lecture_name = serializers.CharField(source='lecture.name', read_only=True)
    
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = StudentLecture
        fields = [
            'id',
            'student',
            'student_username',
            'lecture',
            'lecture_name',
            'status',
            'status_display',
            'created',
        ]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=StudentLecture.objects.all(),
                fields=['student', 'lecture'],
                message="Progress already exists for this student and lecture."
            )
        ]

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'user', 'username', 'full_name', 'created']
        read_only_fields = ['user']

    def get_full_name(self, obj):
        return obj.user.get_full_name()
