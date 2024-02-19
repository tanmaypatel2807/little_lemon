from django.test import TestCase

# Create your tests here.
from .models import Menu, Bookings

class MenuModelTestCase(TestCase):
    def test_menu_item_creation(self):
        item = Menu.objects.create(name='Test Item', price=10.99, description='Test description')
        self.assertEqual(item.name, 'Test Item')

class BookingModelTestCase(TestCase):
    def test_booking_creation(self):
        booking = Bookings.objects.create(table_number=1, date='2022-01-01', time='12:00:00', party_size=4)
        self.assertEqual(booking.table_number, 1)