# sweets_shop/forms.py

from django import forms
from .models import Complaint, Shop

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['description']  # Only include description

    zone = forms.CharField(max_length=100, label='Zone Number', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    location = forms.CharField(max_length=255, label='Location', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    phone_number = forms.CharField(max_length=10, label='Phone Number', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def __init__(self, *args, **kwargs):
        shop = kwargs.pop('shop', None)
        super().__init__(*args, **kwargs)
        if shop:
            self.fields['zone'].initial = shop.zone.name
            self.fields['location'].initial = shop.location
            self.fields['phone_number'].initial = shop.phone_number
