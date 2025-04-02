from django.urls import path
from .views import adminConsole, editBulkPoint,managementUpdateBulk, bulksms,editBulk,editSingle,get_active_orders,riderLoginAddition,managementUpdate,adminConsole, riderAddition, riderDelete, pastProcessedRequest, riderUpdate, requestManagementConsole


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
       path('editSingle/<str:unique_id>/',editSingle,name='editSingle'),
       path('editbulk/<str:unique_id>/',editBulk,name="editBulk"),
       path('editbp/<str:unique_id>/',editBulkPoint,name='editbp'),
        path('bulk/sms/',bulksms,name='bulksms'),
       ]
urlpatterns += [
    path('adminconsole/',adminConsole,name='adminConsole'),
]