
from django.test import TestCase
from .models import Subject, Booking
from django.contrib.auth.models import User

class BookingTestCase(TestCase):

    def setUp(self):

        user1 = User.objects.create(first_name = "Woraphat", last_name = "Wannaphong")
        courseNum2 = Subject.objects.create(class_number = "CN331", subject_name="Software Engineering", capacity=1)

        Booking.objects.create(
            user=user1, course_number=courseNum2
        )
    
    def test_seat_available(self):
        cn320 = Subject.objects.first()
        self.assertTrue(cn320.is_seat_available())

    def test_seat_not_available(self):
        cn320 = Subject.objects.first()
        self.assertFalse(cn320.is_seat_not_available())


# Create your tests here.
