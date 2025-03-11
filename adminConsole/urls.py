from django.urls import path
from .views import adminConsole, managementUpdateBulk, get_active_orders,riderLoginAddition,managementUpdate,adminConsole, riderAddition, riderDelete, pastProcessedRequest, riderUpdate, requestManagementConsole


urlpatterns = [
    path('requestmanagement/',requestManagementConsole,name='requestManagement'),
    path('managementUpdate/<str:unique_id>/',managementUpdate,name='managementUpdate'),
    path('adminConsole/',adminConsole,name='adminConsole'),
    path('riderAdditon/',riderAddition,name='riderAddition'),
    path('riderDelete/<str:unique_id>/',riderDelete,name='riderDelete'),
    path('riderUpdate/<str:unique_id>/',riderUpdate,name="riderUpdate"),
  
    path('pastRequests/',pastProcessedRequest,name='pastProcessedRequest'),
    path('managementUpdateBulk/<str:unique_id>/',managementUpdateBulk,name='managementUpdateBulk'),
    path('riderLoginAddition/<str:unique_id>/',riderLoginAddition,name='riderLoginAddition'),
       path('api/active-orders/', get_active_orders, name='active_orders'),
]
urlpatterns += [
    path('adminconsole/',adminConsole,name='adminConsole'),
]