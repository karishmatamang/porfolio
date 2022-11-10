from .models import PersonalPorfolio
from django import forms


class Personal_form(forms.ModelForm):
    class Meta:
        model=PersonalPorfolio
        fields=['firstname','lastname','profession','email','address','contact','profile']