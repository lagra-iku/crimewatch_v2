from django.db import models
import random
import string
from officers.models import Officer
# from phonenumber_field.modelfields import PhoneNumberField
from cases.models import CriminalCase
from django.utils import timezone

def generate_case_number():
    """Helper function to generate a random case number for a criminal record"""
    letter = string.ascii_letters
    numbers = string.digits
    letters = letter.upper()
    return ''.join(random.choices(letters, k=2)) +'-'+ ''.join(random.choices(numbers, k=6))

class CriminalRecord(models.Model):
    """Criminal's personal information Class"""
    MARITAL_STATUS = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
        ('Widower', 'Widower'),
        ('Celibate', 'Celibate'),
    ]

    RELIGION = [
        ('Christianity', 'Christianity'),
        ('Islam', 'Islam'),
        ('Traditional Worshippers', 'Traditional Worshippers'),
        ('Others', 'Others'),
    ]

    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_arrest = models.DateField(auto_now_add=True)
    time_of_arrest = models.TimeField(auto_now_add=True)
    tribe = models.CharField(max_length=100)
    religion = models.CharField(max_length=100, choices=RELIGION, blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS, default="Single")
    height_in_meters = models.FloatField()
    weight_in_kg = models.FloatField()
    gender = models.CharField(max_length=10, choices=SEX_CHOICES, default="Male")
    nin = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255, blank=True)
    associated_cases = models.ForeignKey(CriminalCase, on_delete=models.CASCADE, blank=True, null=True)
    contact_info = models.CharField(max_length=100, blank=True)
    distinctive_features = models.CharField(max_length=255, blank=True)
    next_of_kin = models.CharField(max_length=255, blank=True)
    mugshot = models.ImageField(upload_to='src/images/', blank=True)
    known_aliases = models.CharField(max_length=255, blank=True)
    associates = models.CharField(max_length=255, blank=True)
    arresting_officer = models.ForeignKey(Officer, on_delete=models.CASCADE, blank=True)
    case_number = models.CharField(max_length=9, default=generate_case_number, unique=True)
    is_incarcerated = models.BooleanField(default=True)
    is_wanted = models.BooleanField(default=False)
    
    def date(self, *args, **kwargs):
        if self.date_of_arrest and timezone.is_naive(self.date_of_arrest):
            self.date_of_arrest = timezone.make_aware(self.date_of_arrest, timezone.get_current_timezone())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Case Number: {self.case_number}, Name: {self.first_name} {self.middle_name} {self.surname}, Arresting Officer: {self.arresting_officer}, Date: {self.date_of_birth}, {self.tribe}, {self.religion}, {self.marital_status}, {self.height_in_meters}, {self.weight_in_kg}"
  
  
class LogIn(models.Model):
    """Class to hold login information"""
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username}, {self.password}"