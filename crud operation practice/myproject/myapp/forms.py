from django.forms import ModelForm
from django import forms
from .models import Borders  # Make sure this import is correct

class BorderForm(ModelForm):
    class Meta:
        model = Borders
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control','type': 'date'}),
        }
