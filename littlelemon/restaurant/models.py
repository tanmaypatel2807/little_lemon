from django.db import models

# Create your models here.
class Bookings(models.Model):
    Booking_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    No_of_guests = models.IntegerField(6)
    Booking_Date = models.DateField()

class Menu(models.Model):
    Menu_ID = models.AutoField(primary_key=True, default=0)
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(5)
