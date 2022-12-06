from django import forms
from .models import Exhibitions
from . models import Arts

class ExhibitionsForm(forms.ModelForm):
    class Meta:
        model = Exhibitions
        fields = ['exhibition_year']
        exhibition_year=forms.CharField()
        content= forms.CharField()
        
class ArtsForm(forms.ModelForm):
    class Meta:
        model = Arts
        fields = ['art_type']
        art_type=forms.CharField()
        content=forms.CharField()