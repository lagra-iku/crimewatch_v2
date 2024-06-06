from django.contrib import admin
from cases.models import CrimeType, CrimeSubcategory, CriminalCase
from criminals.models import CriminalRecord
from officers.models import Officer


admin.site.site_header = "CrimeWatch Administration"
admin.site.site_title = "CrimeWatch Administration Portal"
admin.site.index_title = "Welcome to the CrimeWatch Administration Dashboard"

admin.site.register(Officer)
admin.site.register(CriminalRecord)
admin.site.register(CrimeType)
admin.site.register(CrimeSubcategory)
admin.site.register(CriminalCase)
