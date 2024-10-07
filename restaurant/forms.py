from django import forms
from .models import Restaurant, Food



class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields =['name','address','description','opening_hours','image']


class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ['name','description','price','image']