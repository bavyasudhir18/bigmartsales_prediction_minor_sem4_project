# sales/forms.py
from django import forms
from .models import SalesData

class SalesDataForm(forms.ModelForm):
    class Meta:
        model = SalesData
        exclude = ['Item_Outlet_Sales']  # Exclude prediction field
