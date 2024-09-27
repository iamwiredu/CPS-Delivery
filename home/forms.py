from .models import Profile, Restaurant
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model =  Profile
        fields = ['phone',]

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        labels = {
            'restaurantName':'Restaurant Name',
            'restaurantLocation': 'Restaurant Location',
        }
        fields = ['restaurantName','restaurantLocation']
