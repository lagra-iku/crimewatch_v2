from django.db import models
from officers.models import Officer
from django.utils import timezone
# from criminals.models import CriminalRecord

class CrimeType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CrimeSubcategory(models.Model):
    crime_type = models.ForeignKey(CrimeType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CriminalCase(models.Model):
    CASE_STATUS_CHOICES = [
        ('active', 'Active'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    case_number = models.CharField(max_length=12, unique=True, editable=False)
    event_date = models.DateTimeField()
    crime_type = models.ForeignKey(CrimeType, on_delete=models.CASCADE)
    crime_subcategory = models.ForeignKey(CrimeSubcategory, on_delete=models.CASCADE)
    location_of_crime = models.CharField(max_length=255)
    case_description = models.TextField()
    #associated_case_files = models.ForeignKey(CriminalRecord.case_number, on_delete=models.CASCADE, blank=True)
    # associated_case_files = models.OneToOneField(CriminalRecord, on_delete=models.CASCADE, blank=True, null=True)
    witnesses = models.CharField(max_length=255)
    known_suspects = models.CharField(max_length=255)
    arrested_suspects = models.CharField(max_length=255)
    case_status = models.CharField(max_length=12, choices=CASE_STATUS_CHOICES)
    pictures_of_evidence = models.ImageField(upload_to='src/images/', null=True, blank=True)
    case_officer = models.ForeignKey(Officer, on_delete=models.CASCADE, null=True)


    def save(self, *args, **kwargs):
        if not self.case_number:
            self.case_number = self._generate_case_number()
        super().save(*args, **kwargs)

    def _generate_case_number(self):
        import random
        import string
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    
    def date(self, *args, **kwargs):
        if self.event_date and timezone.is_naive(self.event_date):
            self.event_date = timezone.make_aware(self.event_date, timezone.get_current_timezone())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.case_number
