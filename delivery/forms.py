from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import ModelForm
from .models import DeliveryRequest




class DeliveryRequestForm(ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ['orderQuantity','pickupNumber','pickupPoint','dropoffNumber','deliveryPoint','productFee','additionalInfo']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','activePhoneNumber','password1','password2')
