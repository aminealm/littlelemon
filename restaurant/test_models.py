from django.test import TestCase
from datetime import datetime
from .models import Booking


class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.booking = Booking.objects.create(
            name='test_book',
            no_of_guests=10,
            booking_date = datetime.now()
        )

    def test_fields(self):
        self.assertIsInstance(self.booking.name, str)
        self.assertIsInstance(self.booking.no_of_guests, int)

    def test_timestamps(self):
        self.assertIsInstance(self.booking.booking_date, datetime)