from django import forms
from .models import BirthChartRequest

class BirthChartRequestForm(forms.ModelForm):
    class Meta:
        model = BirthChartRequest
        fields = [
            'full_name', 'email', 'birth_date', 'birth_time', 'birth_place', 'question'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'birth_time': forms.TimeInput(attrs={'type': 'time'}),
        }
