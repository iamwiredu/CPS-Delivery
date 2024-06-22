from django import forms
from django.forms import ModelForm
from delivery.models import Rider
from delivery.models import ShopItem

class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ['name','phone']

class ShopItemForm(forms.ModelForm):
    class Meta:
        model = ShopItem
        fields = ['name','description','price','image']


