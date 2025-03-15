import ast
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View
from .models import DeliveryRequest, BulkDeliveryPoint, BulkDeliveryRequest, QrIdent, Rider
from .forms import DeliveryRequestForm, BulkDeliveryRequestForm, BulkDeliveryPointForm
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.forms import formset_factory
from django.contrib.auth.forms import PasswordChangeForm
from adminConsole.forms import RequestStatusUpdateForm, BulkRequestStatusUpdateForm
# Create your views here.

class accountHome(LoginRequiredMixin,View):
    login_url = '/login/'

    def get(self,request):
        return render(request,'accountHome.html')
    

class RequestPage(LoginRequiredMixin,View):
    login_url = '/login/'
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
                    if request.user.is_authenticated:
                        event.user = request.user
                        event.save()
                    else:
                        event.save()
                    return redirect('/deliveryRequest/')
                else:
                    print('error')
                    # return redirect('/deliveryRequest/')  #pending Request
            if 'addBulkRequest' in request.POST:
                form =  BulkDeliveryRequestForm(request.POST)
                quantity = request.POST.get('quantity')
                deliveryPoints = ast.literal_eval(request.POST.get('objectInput'))
                print(deliveryPoints, type(deliveryPoints))
                if form.is_valid():
                    event = form.save(commit=False)
                    if request.user.is_authenticated:
                        event.user = request.user
                        event.orderQuantity = int(quantity)
                        event.save()
                    else:
                        event.orderQuantity = int(quantity)
                        event.save()

                for deliveryPoint in deliveryPoints:
                    deliveryPointObj = BulkDeliveryPoint(bulkDeliveryRequest=event,deliveryPoint=deliveryPoint[2],dropoffNumber=deliveryPoint[0],dropoffName=deliveryPoint[1],deliveryLocation=deliveryPoint[3],additionalInfo=deliveryPoint[4])

                    deliveryPointObj.save()
                    print('saved')



                    


            
        return render(request,'request.html',self.context)
    

class pastDeliveries(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        DeliveryRequests = DeliveryRequest.objects.filter(user=request.user,delivered=True)
        DeliveryRequestBulk = BulkDeliveryRequest.objects.filter(user=request.user,delivered=True)
        context={
            'DeliveryRequests':DeliveryRequests,
            'DeliveryRequestBulk':DeliveryRequestBulk,
        }
        return render(request,'pastDeliveries.html',context)
    
    


class pendingRequest(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        DeliveryRequests = DeliveryRequest.objects.filter(user=request.user,delivered=False)
        DeliveryRequestBulk = BulkDeliveryRequest.objects.filter(user=request.user,delivered=False)
        context={
            'DeliveryRequests':DeliveryRequests,
            'DeliveryRequestBulk':DeliveryRequestBulk,
        }
        return render(request,'pendingRequests.html',context)
    
class detailsPage(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,pk):
        DeliveryRequested = DeliveryRequest.objects.get(pk=pk)
        DeliveryRequestedForm = DeliveryRequestForm(instance=DeliveryRequested)
        context={
            'DeliveryRequested':DeliveryRequested,
            'DeliveryRequestedForm':DeliveryRequestedForm,
        }
        return render(request,'requestDetails.html',context)
    
class logoutPage(View):
    def get(self,request):
        logout(request)
        return redirect('/login')
    
class comingSoon(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        return render(request,'comingSoon.html')

# Pending details Page

class bulkPendingDetails(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,unique_id):
        DeliveryRequested = BulkDeliveryRequest.objects.get(unique_id=unique_id)
        context ={
            'DeliveryRequested':DeliveryRequested,
        }
        return render(request,'bulkPendingDetails.html',context)
    
from django.forms import formset_factory
from django.shortcuts import render, redirect

def requestMod(request):
    # Individual forms
    DeliveryRequestFormCreator = DeliveryRequestForm()
    BulkDeliveryRequestFormCreator = BulkDeliveryRequestForm()

    # Formset for bulk delivery points


    if request.method == 'POST':
        if 'addBulkRequest' in request.POST:
            # Get the number of delivery points from the form
            number_of_points = int(request.POST.get('objectInput'))
           
            bulksender = BulkDeliveryRequestForm(request.POST)
          
            if bulksender.is_valid():
                event = bulksender.save(commit=False)
                if request.user.is_authenticated:
                     event.user = request.user
                     event.orderQuantity = number_of_points
                     event.save()
               
                else:
                    event.orderQuantity = number_of_points
                    event.save()
                
                

                for i in range(1, number_of_points+1):
                   
                 
                    dropoff_number = request.POST.get(f'dropoffNumber_bulk_{i}')
                    dropoff_name = request.POST.get(f'id_dropoffName_bulk_{i}')
                    delivery_point = request.POST.get(f'deliveryPoint_bulk_{i}')
                    dropoff_area = request.POST.get(f'id_dropoffArea_bulk_{i}')
                    delivery_speed = request.POST.get(f'delivery_speed_{i}')
                    additional_info = request.POST.get(f'additionalInfo_bulk_{i}', '')
                    print(dropoff_number,dropoff_name,delivery_point,dropoff_area,additional_info,delivery_speed)
                    point = BulkDeliveryPoint(bulkDeliveryRequest=event,deliveryPoint=delivery_point,dropoffNumber=dropoff_number,dropoffName=dropoff_name,deliveryLocation=dropoff_area,deliverySpeed=delivery_speed,additionalInfo=additional_info)
                    point.save()
                
                messages.success(request,'Order Placed.')
                if request.user.is_authenticated:
                    return redirect('/pendingRequest/')
                else:
                    return redirect('/quickPlaced/')

        if 'createRequest' in request.POST:
            DeliveryRequestFormCreator = DeliveryRequestForm(request.POST)
            if DeliveryRequestFormCreator.is_valid():
                event = DeliveryRequestFormCreator.save(commit=False)
                if request.user.is_authenticated:
                    event.user = request.user
                    event.save()
                else:
                    event.save()
                print(event)
                qrcodeData = QrIdent(deliveryRequest=event,requestType='single')
                qrcodeData.save()
                messages.success(request,'Order Placed.')
                if request.user.is_authenticated:
                    return redirect('/pendingRequest/')
                else:
                    return redirect('/quickPlaced/')
            else:
                print('error')
                    # return redirect('/deliveryRequest/')  #pending Request
    else:
        # Display empty formset initially
        print('error')

    # Pass forms and formset to the template context
    context = {
        'DeliveryRequestFormCreator': DeliveryRequestFormCreator,
        'BulkDeliveryRequestFormCreator': BulkDeliveryRequestFormCreator,
      
    }
    
    return render(request, 'requestMod.html', context)

def receiptPage(request,unique_id):
    deliveryRequest = DeliveryRequest.objects.get(unique_id=unique_id)
    context ={
        'deliveryRequest':deliveryRequest,
    }
    
    return render(request,'receipt.html',context)

def receiptPageBulk(request,unique_id):
    deliveryRequest = BulkDeliveryRequest.objects.get(unique_id=unique_id)
    context ={
        'deliveryRequest':deliveryRequest,
    }
    return render(request,'receiptBulk.html',context)

def deliveryVal(request,unique_id):
    deliveryRequest = DeliveryRequest.objects.get(unique_id=unique_id)
    context ={
        'deliveryRequest':deliveryRequest,
    }
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        rider = Rider.objects.get(user=user)
        if user  and rider:  # Check if user is a rider
            login(request, user)  # Log the user in
            return redirect(f'/updateSingle/{unique_id}')
        
    return render(request, "deliveryVal.html",context)  # Render the HTML page

def bulkDeliveryVal(request,unique_id):
    deliveryRequest = BulkDeliveryRequest.objects.get(unique_id=unique_id)
    context ={
        'deliveryRequest':deliveryRequest,
    }
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        rider = Rider.objects.get(user=user)
        if user  and rider:  # Check if user is a rider
            login(request, user)  # Log the user in
            return redirect(f'/updateBulk/{unique_id}')
        
    return render(request, "bulkDeliveryVal.html",context)  # Render the HTML page



def update_order_single(request,unique_id):
    deliveryRequest = DeliveryRequest.objects.get(unique_id=unique_id)
    requestStatusUpdateForm = RequestStatusUpdateForm(instance=deliveryRequest)

    context ={
        'requestStatusUpdateForm':requestStatusUpdateForm,
    }
    
    if 'updateRequest' in request.POST:
        form = RequestStatusUpdateForm(request.POST,instance=deliveryRequest)
        if form.is_valid():
            form.save()
            print('saved')
            if deliveryRequest.pickedUp == True:
                deliveryRequest.enroute = True
                deliveryRequest.save()
            else:
                deliveryRequest.enroute = False
                deliveryRequest.save()
            if deliveryRequest.delivered == True:
                deliveryRequest.pickedUp = True
                deliveryRequest.enroute = True
                deliveryRequest.save()
                
            
        else:
            print('Error')
        return redirect(update_order_single,unique_id)

    return render(request,'updateSingle.html',context)

def update_order_bulk(request,unique_id):
    deliveryRequest = BulkDeliveryRequest.objects.get(unique_id=unique_id)
    requestStatusUpdateForm = BulkRequestStatusUpdateForm(instance=deliveryRequest)

    context ={
        'requestStatusUpdateForm':requestStatusUpdateForm,
    }
    
    if 'updateRequest' in request.POST:
        form = RequestStatusUpdateForm(request.POST,instance=deliveryRequest)
        if form.is_valid():
            form.save()
            print('saved')
            if deliveryRequest.pickedUp == True:
                deliveryRequest.enroute = True
                deliveryRequest.save()
            else:
                deliveryRequest.enroute = False
                deliveryRequest.save()
            if deliveryRequest.delivered == True:
                deliveryRequest.pickedUp = True
                deliveryRequest.enroute = True
                deliveryRequest.save()
                
            
        else:
            print('Error')
        return redirect(update_order_bulk,unique_id)

    return render(request,'updateBulk.html',context)
    
   

def update_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        
        # Assuming rider is authenticated and order_id is sent
        order = DeliveryRequest.objects.get(id=data["order_id"])
        
        if data.get("pickedUp"):
            order.status = "Picked Up"
        if data.get("delivered"):
            order.status = "Delivered"
        
        order.save()
        return JsonResponse({"success": True})

def rulesPolicies(request):
    return render(request,'rulesPolicies.html')

def settingsPage(request):
    return render(request,'settingsPage.html')

def quickPlaced(request):
    return render(request,'quickPlaced.html')