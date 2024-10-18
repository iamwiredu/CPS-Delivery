
from django.views.generic import TemplateView
# Create your views here.

from django.shortcuts import render, redirect
from delivery.models import DeliveryRequest,Rider, BulkDeliveryRequest, BulkDeliveryPoint
from .forms import RiderForm, ShopItemForm, RequestStatusUpdateForm, RidersAssignmentForm, BulkRidersAssignmentForm, BulkRequestStatusUpdateForm
from delivery.models import ShopItem
from home.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests
# Create your views here.

@login_required(login_url='/login/')
def adminConsole(request):
    if request.user.is_superuser:
        return render(request,'admin.html')
    else:
        return redirect('/accounthome/')


@login_required(login_url='/login/')
def requestManagementConsole(request):
    DeliveryRequests = DeliveryRequest.objects.filter(delivered=False).order_by('id')
    BulkDeliveryRequests = BulkDeliveryRequest.objects.filter(delivered=False).order_by('id')
    riders = Rider.objects.all()
    print(DeliveryRequests)
    context ={
        'DeliveryRequests':DeliveryRequests,
        'BulkDeliveryRequests':BulkDeliveryRequests,
        'riders':riders,

    }
    if request.method == 'POST':
        if 'updateSingleOrder' in request.POST:
            
            request_id = request.POST.get('request_id')
            assigned = request.POST.get('assigned')
            pickedUp = request.POST.get('pickedUp')
            enroute = request.POST.get('enroute')
            delivered = request.POST.get('delivered')
            selectedRider = request.POST.get('rider')
        

            # Fetch the delivery request based on the rider_id
            request_single = DeliveryRequest.objects.get(unique_id=request_id)
            print(selectedRider)
            # Update 'assigned' field

            # Update 'pickedUp' field
            if pickedUp == 'on':
                request_single.pickedUp = True
            else:
                request_single.pickedUp = False

            # Update 'enroute' field
            if enroute == 'on':
                request_single.enroute = True
            else:
                request_single.enroute = False

            # Update 'delivered' field
            if delivered == 'on':
                request_single.delivered = True
            else:
                request_single.delivered = False

            # Save the updated request object to the database
            if not request_single.rider: 
                rider = Rider.objects.get(unique_id=selectedRider)
                request_single.rider = rider
                request_single.assigned = True
            request_single.save()
            return redirect('/requestmanagement/')
        if 'updateBulkOrder' in request.POST:
            
            request_id = request.POST.get('request_id')
            assigned = request.POST.get('assigned')
            pickedUp = request.POST.get('pickedUp')
            enroute = request.POST.get('enroute')
            delivered = request.POST.get('delivered')
            selectedRider = request.POST.get('rider')
        

            # Fetch the delivery request based on the rider_id
            request_bulk = BulkDeliveryRequest.objects.get(unique_id=request_id)
            print(selectedRider)
            # Update 'assigned' field

            # Update 'pickedUp' field
            if pickedUp == 'on':
                request_bulk.pickedUp = True
            else:
                request_bulk.pickedUp = False

            # Update 'enroute' field
            if enroute == 'on':
                request_bulk.enroute = True
            else:
                request_bulk.enroute = False

            # Update 'delivered' field
            if delivered == 'on':
                request_bulk.delivered = True
            else:
                request_bulk.delivered = False

            # Save the updated request object to the database
            if not request_bulk.rider: 
                rider = Rider.objects.get(unique_id=selectedRider)
                request_bulk.rider = rider
                request_bulk.assigned = True
            request_bulk.save()



    return render(request,'html/requestsManagementConsole.html',context)



@login_required(login_url='/login/')
def pastProcessedRequest(request):
    DeliveryRequests = DeliveryRequest.objects.filter(delivered=True).values()
    context ={
        'DeliveryRequests':DeliveryRequests,

    }
    return render(request,'html/pastProcessedRequest.html',context)
def AssignedRiderMsg(instance,rider):
    endPoint = 'https://api.mnotify.com/api/sms/quick'
    apiKey = '	SncBkQH0xepW3ACOlCty3AjUX'
    data = {
    'recipient[]': [str(instance.pickupNumber)],
    'sender': 'CPS',
    'message': f'Your request for CPS deliveries service with ORDER ID: 00{instance.id} has been assigned to rider {rider.name} .Contact him on 0{rider.phone}',
    'schedule_date': '',
    }
    url = endPoint + '?key=' + apiKey
    response = requests.post(url, data)
    data = response.json() 
    print(data,str(instance.pickupNumber))

@login_required(login_url='/login/')
def managementUpdate(request,unique_id):
    Riders = Rider.objects.all()
    DeliveryRequested = DeliveryRequest.objects.get(unique_id=unique_id)
    RequestStatusUpdateFormUpdater = RequestStatusUpdateForm(instance=DeliveryRequested)
    RidersAssignmentFormUpdater = RidersAssignmentForm(instance=DeliveryRequested)


    
    if request.method == 'POST':
        if 'UdpateAssignment' in request.POST:
            form = RidersAssignmentForm(request.POST,instance=DeliveryRequested)
            rider = request.POST.get('rider')
            AssignedRider = Rider.objects.get(id=rider)
            
            if form.is_valid():
                form.save()
                AssignedRiderMsg(DeliveryRequested,AssignedRider)
                DeliveryRequested.assigned = True
                DeliveryRequested.save()
                print('Done')
            else:
                print('Error')
            return redirect(managementUpdate,unique_id)
        if 'UpdateRequest' in request.POST:
            form = RequestStatusUpdateForm(request.POST,instance=DeliveryRequested)


            if form.is_valid():
                form.save()
                if DeliveryRequested.pickedUp == True:
                    DeliveryRequested.enroute = True
                    DeliveryRequested.save()
                else:
                    DeliveryRequested.enroute = False
                    DeliveryRequested.save()
                if DeliveryRequested.delivered == True:
                    DeliveryRequested.pickedUp = True
                    DeliveryRequested.enroute = True
                    DeliveryRequested.save()
                    
                
            else:
                print('Error')
            return redirect(managementUpdate,unique_id)


    context = {
        'DeliveryRequested':DeliveryRequested,
        'RequestStatusUpdateFormUpdater':RequestStatusUpdateFormUpdater,
        'Riders':Riders,
        'RidersAssignmentFormUpdater':RidersAssignmentFormUpdater,

    }
    return render(request,'html/managementUpdate.html',context)


@login_required(login_url='/login/')
def riderAddition(request):
    Riders = Rider.objects.all()
    RiderAdditionFormCreator = RiderForm()
    if request.method == 'POST':
        if 'addRider' in request.POST:
            RiderAdditionFormCreator = RiderForm(request.POST)
            if RiderAdditionFormCreator.is_valid():
                RiderAdditionFormCreator.save()
                return redirect(adminConsole)
    context = {
        'RiderAdditionFormCreator':RiderAdditionFormCreator,
        'Riders':Riders,
    }

    return render(request,'html/riderAddition.html',context)


@login_required(login_url='/login/')
def riderDelete(request,unique_id):
    rider = Rider.objects.get(unique_id=unique_id)
    rider.delete()
    return redirect(riderAddition)


@login_required(login_url='/login/')
def riderUpdate(request,unique_id):
    rider = Rider.objects.get(unique_id=unique_id)
    DeliveryRequestsUnassigned = DeliveryRequest.objects.filter(assigned=False).values()
    DeliveryRequestsAssigned = DeliveryRequest.objects.filter(assigned=True,rider=rider).values()
    DeliveryRequestsDelivered = DeliveryRequest.objects.filter(delivered=True,rider=rider).values()
    RiderFormUpdate = RiderForm(instance=rider)

    if request.method == 'POST':
        if 'updateRider' in request.POST:
            RiderFormUpdate = RiderForm(request.POST,instance=rider)
            if RiderFormUpdate.is_valid():
                RiderFormUpdate.save()
                return redirect(riderUpdate,unique_id)
        if 'assignRider' in request.POST:
            unique_id_request = request.POST.get('unique_id')
            DeliveryRequested = DeliveryRequest.objects.get(unique_id=unique_id_request)
            DeliveryRequested.rider = rider
            DeliveryRequested.assigned = True
            DeliveryRequested.save()
            AssignedRiderMsg(DeliveryRequested,rider)
            print(DeliveryRequested.rider)
            return redirect(riderUpdate,unique_id)
        if 'unassignRider' in request.POST:
            unique_id_request = request.POST.get('unique_id')
            DeliveryRequested = DeliveryRequest.objects.get(unique_id=unique_id_request)
            DeliveryRequested.rider = None
            DeliveryRequested.assigned = False
            DeliveryRequested.save()
            return redirect(riderUpdate,unique_id)



    context={
        'rider':rider,
        'RiderFormUpdate':RiderFormUpdate,
        'DeliveryRequestsUnassigned':DeliveryRequestsUnassigned,
        'DeliveryRequestsAssigned':DeliveryRequestsAssigned,
        'DeliveryRequestsDelivered':DeliveryRequestsDelivered,
    }

    return render(request,'html/riderUpdate.html',context)

@login_required(login_url='/login/')
def addShopItem(request):
    ShopItemFormCreator = ShopItemForm()
    ShopItems  = ShopItem.objects.all()
    if request.method == 'POST': 
        if 'addShopItem'  in request.POST:
            form = ShopItemForm(request.POST, request.FILES)  
            if form.is_valid():  
                form.save()
                return redirect(addShopItem)
            else:
                print('Error')
        
    context={
        'ShopItemFormCreator':ShopItemFormCreator,
        'ShopItems':ShopItems,
    }
    return render(request,'html/addShopItem.html',context)

@login_required(login_url='/login/')
def riderLoginAddition(request,unique_id):
    rider = Rider.objects.get(unique_id=unique_id)
    if request.method == 'POST':
        if 'addRider' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create(username=username)

            user.set_password(password)
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.user = user
            profile.accountType = 'Rider'
            profile.rider = rider
            profile.save()

            return redirect(f'/riderUpdate/{unique_id}')

    context={
        'rider':rider,
    }
    return render(request,'html/riderSignup.html',context)


@login_required(login_url='/login/')
def managementUpdateBulk(request,unique_id):
    DeliveryRequested = BulkDeliveryRequest.objects.get(unique_id=unique_id)
    BulkRequestStatusUpdateFormUpdater = BulkRequestStatusUpdateForm()
    BulkRidersAssignmentFormUpdater = BulkRidersAssignmentForm()
    if request.method == 'POST':
        if 'UdpateAssignment' in request.POST:
            form = RidersAssignmentForm(request.POST,instance=DeliveryRequested)
            rider = request.POST.get('rider')
            AssignedRider = Rider.objects.get(id=rider)
            
            if form.is_valid():
                form.save()
                AssignedRiderMsg(DeliveryRequested,AssignedRider)
                DeliveryRequested.assigned = True
                DeliveryRequested.save()
                print('Done')
            else:
                print('Error')
            return redirect(managementUpdateBulk,unique_id)
        if 'UpdateRequest' in request.POST:
            form = BulkRequestStatusUpdateForm(request.POST,instance=DeliveryRequested)


            if form.is_valid():
                form.save()
                if DeliveryRequested.pickedUp == True:
                    DeliveryRequested.enroute = True
                    DeliveryRequested.save()
                else:
                    DeliveryRequested.enroute = False
                    DeliveryRequested.save()
                if DeliveryRequested.delivered == True:
                    DeliveryRequested.pickedUp = True
                    DeliveryRequested.enroute = True
                    DeliveryRequested.save()
                    
                
            else:
                print('Error')
            return redirect(managementUpdateBulk,unique_id)
    context ={
        'DeliveryRequested':DeliveryRequested,
        'BulkRequestStatusUpdateFormUpdater':BulkRequestStatusUpdateFormUpdater,
        'BulkRidersAssignmentFormUpdater':BulkRidersAssignmentFormUpdater,
        }
    return render(request,'html/managementUpdateBulk.html',context)