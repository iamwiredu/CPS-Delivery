from .models import Profile, Restaurant
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model =  Profile
        fields = ['phone',]

