from django import forms
from .models import CriminalCase, CrimeType, CrimeSubcategory
from django.http import JsonResponse

class CriminalCaseForm(forms.ModelForm):
    class Meta:
        model = CriminalCase
        fields = '__all__'
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CriminalCaseForm, self).__init__(*args, **kwargs)
        self.fields['crime_subcategory'].queryset = CrimeSubcategory.objects.none()

        if 'crime_type' in self.data:
            try:
                crime_type_id = int(self.data.get('crime_type'))
                self.fields['crime_subcategory'].queryset = CrimeSubcategory.objects.filter(crime_type_id=crime_type_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and use empty queryset
        elif self.instance.pk:
            self.fields['crime_subcategory'].queryset = self.instance.crime_type.crimesubcategory_set.order_by('name')
