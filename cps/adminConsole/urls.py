from django.urls import path
from .views import requestManagementConsole, managementUpdate,adminConsole, riderAddition, riderDelete, pastProcessedRequest, riderUpdate, addShopItem

urlpatterns = [
    path('requestmanagement/',requestManagementConsole,name='requestManagement'),
    path('managementUpdate/<str:unique_id>/',managementUpdate,name='managementUpdate'),
    path('adminConsole/',adminConsole,name='adminConsole'),
    path('riderAdditon/',riderAddition,name='riderAddition'),
    path('riderDelete/<str:unique_id>/',riderDelete,name='riderDelete'),
    path('riderUpdate/<str:unique_id>/',riderUpdate,name="riderUpdate"),
    path('addShopItem/',addShopItem,name='addShopItem'),
    path('pastRequests/',pastProcessedRequest,name='pastProcessedRequest')
]