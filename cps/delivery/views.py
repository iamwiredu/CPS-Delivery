from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DeliveryRequestForm
from .models import DeliveryRequest

# Create your views here.

def homePage(request):
    return render(request,'html/homepage.html')

def requestPage(request):
    DeliveryRequestFormCreator = DeliveryRequestForm()
    context = {
        'DeliveryRequestFormCreator':DeliveryRequestFormCreator,

    }
    if request.method == 'POST':
        if 'createRequest' in request.POST:
            DeliveryRequestFormCreator = DeliveryRequestForm(request.POST)
            if DeliveryRequestFormCreator.is_valid():
                event = DeliveryRequestFormCreator.save(commit=False)
                event.user = request.user
                event.save()
            return redirect(pendingRequest) 
        
    return render(request,'html/request.html',context)

def pendingRequest(request):
    DeliveryRequests = DeliveryRequest.objects.filter(user=request.user,enroute=False).values()
    print(DeliveryRequests)
    context = {
        'DeliveryRequests':DeliveryRequests,
    }
    return render(request,'html/pendingRequest.html',context)

def pastRequest(request):
    DeliveryRequests = DeliveryRequest.objects.filter(user=request.user,delivered=True).values()
    context={
        'DeliveryRequests':DeliveryRequests,
    }
    return render(request,'html/pastRequest.html',context)

def activeRequest(request):
    DeliveryRequests = DeliveryRequest.objects.filter(user=request.user,enroute=True).values()
    context={
        'DeliveryRequests':DeliveryRequests,
    }
    return render(request,'html/activeRequest.html',context)