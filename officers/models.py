from django.db import models

class Officer(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    RANK_CHOICES = [
        ('Recruit Constable', 'Recruit Constable'),
        ('Constable', 'Constable'),
        ('Corporal', 'Corporal'),
        ('Sergeant', 'Sergeant'),
        ('Sergeant Major', 'Major'),
        ('Inspector', 'Inspector'),
    ]

    DUTY_STATUS = [
        ('On Duty', 'On Duty'),
        ('Off Duty', 'Off Duty'),
    ]

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default="Male")
    rank = models.CharField(max_length=100, choices=RANK_CHOICES, blank=True)
    badge_number = models.IntegerField(unique=True)
    area = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    nationality = models.CharField(max_length=255, default="Nigerian")
    duty_status = models.CharField(max_length=10, choices=DUTY_STATUS, default="On Duty")


    def __str__(self):
        return f"{self.rank} {self.name}"
