from django import forms
from django.forms import ModelForm
from delivery.models import Rider

class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ['name','phone']
