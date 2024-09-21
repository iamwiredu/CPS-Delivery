import ast
from django.shortcuts import render, redirect
from django.views import View
from .models import DeliveryRequest, BulkDeliveryPoint
from .forms import DeliveryRequestForm, BulkDeliveryRequestForm, BulkDeliveryPointForm

# Create your views here.

class accountHome(View):

    def get(self,request):
        return render(request,'accountHome.html')
    

class RequestPage(View):
    DeliveryRequestFormCreator = DeliveryRequestForm()
    BulkDeliveryRequestFormCreator = BulkDeliveryRequestForm()
    BulkDeliveryPointFormCreator = BulkDeliveryPointForm()
    context = {
            'DeliveryRequestFormCreator':DeliveryRequestFormCreator,
            'BulkDeliveryRequestFormCreator':BulkDeliveryRequestFormCreator,
            'BulkDeliveryPointFormCreator':BulkDeliveryPointFormCreator,

        }
    def get(self,request):
    

        return render(request,'request.html',self.context)
    
    def post(self,request):
        if request.method == 'POST':
            if 'createRequest' in request.POST:
                DeliveryRequestFormCreator = DeliveryRequestForm(request.POST)
                if DeliveryRequestFormCreator.is_valid():
                    event = DeliveryRequestFormCreator.save(commit=False)
                    event.user = request.user
                    event.save()
                return redirect('/accounthome/')  #pending Request
            if 'addBulkRequest' in request.POST:
                form =  BulkDeliveryRequestForm(request.POST)
                quantity = request.POST.get('quantity')
                deliveryPoints = ast.literal_eval(request.POST.get('objectInput'))
                print(deliveryPoints, type(deliveryPoints))
                if form.is_valid():
                    event = form.save(commit=False)
                    event.user = request.user
                    event.orderQuantity = int(quantity)
                    event.save()
                for deliveryPoint in deliveryPoints:
                    deliveryPointObj = BulkDeliveryPoint(bulkDeliveryRequest=event,deliveryPoint=deliveryPoint[2],dropoffNumber=deliveryPoint[0],dropoffName=deliveryPoint[1],Location=deliveryPoint[3],additionalInfo=deliveryPoint[4])

                    deliveryPointObj.save()
                    print('saved')



                    


            
        return render(request,'request.html',self.context)
    

class pastDeliveries(View):
    def get(self,request):
        DeliveryRequests = DeliveryRequest.objects.filter(user=request.user,delivered=True)
        context={
            'DeliveryRequests':DeliveryRequests,
        }
        return render(request,'pastDeliveries.html',context)
    
    


class pendingRequest(View):
    def get(self,request):
        DeliveryRequests = DeliveryRequest.objects.filter(user=request.user,delivered=False)
        context={
            'DeliveryRequests':DeliveryRequests,
        }
        return render(request,'pendingRequests.html',context)
    
class detailsPage(View):
    def get(self,request,pk):
        DeliveryRequested = DeliveryRequest.objects.get(pk=pk)
        DeliveryRequestedForm = DeliveryRequestForm(instance=DeliveryRequested)
        context={
            'DeliveryRequested':DeliveryRequested,
            'DeliveryRequestedForm':DeliveryRequestedForm,
        }
        return render(request,'requestDetails.html',context)