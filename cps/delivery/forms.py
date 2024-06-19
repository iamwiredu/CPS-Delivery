from django import forms
from django.forms import ModelForm
from .models import DeliveryRequest

from allauth.account.forms import SignupForm


class DeliveryRequestForm(ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ['orderQuantity','pickupNumber','deliveryPoint','dropoffNumber','pickupPoint','senderNumber','productFee','additionalInfo']

class MyCustomSignupForm(SignupForm):    
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['phone'] = forms.IntegerField(required=True)    
        def save(self, request):
            phone = self.cleaned_data.pop('phone')
            ...
            user = super(MyCustomSignupForm, self).save(request)