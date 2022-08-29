from django import forms
from .models import StockClass

class StockForm(forms.ModelForm):
    class Meta:
        model = StockClass 
        fields = ["ticker"]