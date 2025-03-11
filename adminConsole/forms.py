from django import forms
from django.forms import ModelForm
from delivery.models import Rider
from delivery.models import DeliveryRequest, BulkDeliveryRequest

class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ['name','phone']



class RequestStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ['pickedUp','delivered']

class RidersAssignmentForm(forms.ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ['rider']

class BulkRequestStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = BulkDeliveryRequest
        fields = ['pickedUp','delivered']

class BulkRidersAssignmentForm(forms.ModelForm):
    class Meta:
        model = BulkDeliveryRequest
        fields = ['rider']