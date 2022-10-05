
from django.test import TestCase
from .models import Subject, Booking
from django.contrib.auth.models import User

class BookingTestCase(TestCase):

    def setUp(self):

        user1 = User.objects.create(first_name = "Woraphat", last_name = "Wannaphong")
        courseNum2 = Subject.objects.create(class_number = "CN331", subject_name="Software Engineering")

        Booking.objects.create(
            user=user1, course_number=courseNum2
        )
    
    def test_seats_available(self):
        subject = Subject.objects.first()
        self.assertTrue(subject.is_seat_available())

    ##def test_seats_not_available(self):


# Create your tests here.
