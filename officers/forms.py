from django import forms
from .models import Officer

class OfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_appointment': forms.DateInput(attrs={'type': 'date'}),
            'time_of_appointment': forms.TimeInput(attrs={'type': 'time'}),
        }
