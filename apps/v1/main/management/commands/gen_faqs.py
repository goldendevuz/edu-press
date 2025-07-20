from django.core.management.base import BaseCommand
from apps.v1.course.models import Faq

class Command(BaseCommand):
    help = "Generate sample FAQs for Udemy clone platform"

    def handle(self, *args, **kwargs):
        faqs = [
            {
                "question": "How do I enroll in a course?",
                "answer": "To enroll, visit the course page and click on the 'Enroll Now' button. Follow the instructions to complete your enrollment."
            },
            {
                "question": "Can I get a certificate after completing a course?",
                "answer": "Yes, once you complete all the course requirements, a certificate will be automatically issued and available in your profile."
            },
            {
                "question": "Are the courses self-paced?",
                "answer": "Yes, most courses are self-paced, allowing you to learn at your own speed and convenience."
            },
            {
                "question": "How do I contact the instructor?",
                "answer": "You can contact instructors by using the 'Ask Instructor' feature on the course page or through the Q&A section."
            },
            {
                "question": "Can I access the courses offline?",
                "answer": "At the moment, offline access is not supported. You need an internet connection to watch the video lectures."
            },
            {
                "question": "What is the refund policy?",
                "answer": "We offer a 14-day money-back guarantee if you’re not satisfied with your course."
            },
            {
                "question": "Are there any free courses available?",
                "answer": "Yes, we offer a variety of free courses. Simply filter by 'Free' on the course listing page."
            },
            {
                "question": "Can I use the platform on mobile devices?",
                "answer": "Absolutely! Our platform is fully responsive and works on any smartphone or tablet browser."
            },
        ]

        created = 0
        for faq in faqs:
            obj, created_flag = Faq.objects.get_or_create(question=faq["question"], defaults={"answer": faq["answer"]})
            if created_flag:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"{created} FAQs created successfully."))
