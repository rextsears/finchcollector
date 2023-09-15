from django import forms
from .models import Finch, Feeding, Toy

class FinchForm(forms.ModelForm):
    class Meta:
        model = Finch
        fields = '__all__'

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['feeding_date', 'food_type', 'notes']

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ['name', 'description']