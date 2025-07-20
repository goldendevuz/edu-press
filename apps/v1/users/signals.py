from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model

from apps.v1.course.models import Instructor, Student  

User = get_user_model()


@receiver(pre_save, sender=User)
def handle_role_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # Skip new users

    try:
        old_instance = User.objects.get(pk=instance.pk)
    except User.DoesNotExist:
        return

    old_role = old_instance.user_roles
    new_role = instance.user_roles

    # Demoted from instructor
    if old_role == 'instructor' and new_role != 'instructor':
        try:
            instance.instructor.delete()
        except Instructor.DoesNotExist:
            pass

    # Demoted from student
    if old_role == 'student' and new_role != 'student':
        try:
            instance.students.all().delete()  # related_name = 'students'
        except:
            pass


@receiver(post_save, sender=User)
def create_profile_based_on_role(sender, instance, created, **kwargs):
    if instance.user_roles == 'instructor':
        Instructor.objects.get_or_create(
            user=instance,
            defaults={"name": instance.get_full_name() or instance.username}
        )

    elif instance.user_roles == 'student':
        Student.objects.get_or_create(user=instance)
