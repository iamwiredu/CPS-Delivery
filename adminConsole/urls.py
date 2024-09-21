from django.urls import path
from .views import adminConsole, managementUpdateBulk,managementUpdate,adminConsole, riderAddition, riderDelete, pastProcessedRequest, riderUpdate, addShopItem, requestManagementConsole


urlpatterns = [
    path('requestmanagement/',requestManagementConsole,name='requestManagement'),
    path('managementUpdate/<str:unique_id>/',managementUpdate,name='managementUpdate'),
    path('adminConsole/',adminConsole,name='adminConsole'),
    path('riderAdditon/',riderAddition,name='riderAddition'),
    path('riderDelete/<str:unique_id>/',riderDelete,name='riderDelete'),
    path('riderUpdate/<str:unique_id>/',riderUpdate,name="riderUpdate"),
    path('addShopItem/',addShopItem,name='addShopItem'),
    path('pastRequests/',pastProcessedRequest,name='pastProcessedRequest'),
    path('managementUpdateBulk/<str:unique_id>/',managementUpdateBulk,name='managementUpdateBulk')
]
urlpatterns += [
    path('adminconsole/',adminConsole,name='adminConsole'),
]