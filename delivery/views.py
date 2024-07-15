from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import DeliveryRequestForm
from .models import DeliveryRequest, ShopItem
from adminConsole.views import adminConsole

# Create your views here.

def homePage(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect(adminConsole)
        else:
            return render(request,'html/homepage.html')
    else:
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
    DeliveryRequests = DeliveryRequest.objects.filter(user=request.user,delivered=False)
    print(DeliveryRequests)
    
    context = {
        'DeliveryRequests':DeliveryRequests,
    }
    return render(request,'html/pendingRequest.html',context)

def pastRequest(request):
    DeliveryRequests = DeliveryRequest.objects.filter(user=request.user,delivered=True)
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

def detailsPage(request,unique_id):
    DeliveryRequested = DeliveryRequest.objects.get(unique_id=unique_id)
    DeliveryRequestedForm = DeliveryRequestForm(instance=DeliveryRequested)
    print(DeliveryRequested)
    context={
        'DeliveryRequested':DeliveryRequested,
        'DeliveryRequestedForm':DeliveryRequestedForm,
    }
    return render(request,'html/detailsPage.html',context)


def ShopPage(request):
    ShopItems = ShopItem.objects.all()
    print(len(ShopItems))
    ShopItems_left = []
    for i in range(0,4-len(ShopItems)):
        ShopItems_left.append({'name':'none'})
    print(ShopItems_left)
        
    context = {
        'ShopItems':ShopItems,
        'ShopItems_left':ShopItems_left,

    }

    # return render(request,'html/shopPage.html',context)
    return render(request,'html/comingSoon.html',context)

def StoragePage(request):
    context = {

    }

    # return render(request,'html/storagePage.html',context)
    return render(request,'html/comingSoon.html',context)

def OnlinePharmacy(request):
    context = {

    }

    # return render(request,'html/storagePage.html',context)
    return render(request,'html/comingSoon.html',context)


def automaticLogout(request):
    logout(request)
    return redirect('/accounts/login')
