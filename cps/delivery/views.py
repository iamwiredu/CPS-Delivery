from django.shortcuts import render
from django.http import HttpResponse
from .forms import DeliveryRequestForm

# Create your views here.

def homePage(request):
    return render(request,'html/homepage.html')

def requestPage(request):
    DeliveryRequestFormCreator = DeliveryRequestForm()
    context = {
        'DeliveryRequestFormCreator':DeliveryRequestFormCreator,

    }
    return render(request,'html/request.html',context)