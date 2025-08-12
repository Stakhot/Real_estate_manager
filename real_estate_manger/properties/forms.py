from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['address', 'purchase_price', 'monthly_rent', 'status']
