from django import forms
from django.forms import ModelForm
from .models import DeliveryRequest


class DeliveryRequestForm(ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ['orderQuantity','pickupNumber','deliveryPoint','dropoffNumber','pickupPoint','senderNumber','productFee','additionalInfo']