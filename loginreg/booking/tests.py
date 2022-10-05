""""
from django.test import TestCase
from .models import Subject, Booking

class BookingTestCase(TestCase):

    def setUp(self):

        subject1 = Subject.objects.create(class_number="", subject_name="", section="", semester="", year="", seats="" )
        subject2 = Subject.objects.create(class_number="", subject_name="", section="", semester="", year="", seats="" )

        Booking.objects.create(
            
        )

# Create your tests here."""
