from django import forms
from .models import Finch

class FinchForm(forms.ModelForm):
    class Meta:
        model = Finch
        fields = '__all__'

class FeedingForm(forms.Form):
    feeding_date = forms.DateField(label='Feeding Date')
    food_type = forms.CharField(max_length=100, label='Food Type')
    notes = forms.CharField(widget=forms.Textarea, label='Notes')