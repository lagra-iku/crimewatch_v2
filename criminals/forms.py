from django import forms
from .models import CriminalRecord, LogIn

class CriminalForm(forms.ModelForm):
    """Form for the criminal record model"""
    class Meta:
        model = CriminalRecord
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_arrest': forms.DateInput(attrs={'type': 'date'}),
            'time_of_arrest': forms.TimeInput(attrs={'type': 'time'}),
            'distinctive_features': forms.TextInput(attrs={'placeholder': 'Scars, Tribal marks, Tattoos, Piercings, etc.'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        }


class LogInForm(forms.ModelForm):
    """Form for the login model"""
    class Meta:
        model = LogIn
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }

   
