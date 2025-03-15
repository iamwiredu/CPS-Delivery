from django.urls import path
from .views import accountHome, bulkDeliveryVal, update_order_bulk,requestMod, receiptPageBulk,settingsPage,quickPlaced, rulesPolicies,receiptPage,deliveryVal, update_order_single,bulkPendingDetails,comingSoon,logoutPage,RequestPage,pastDeliveries, pendingRequest, detailsPage

urlpatterns = [
    path('accounthome/',accountHome.as_view(),name='accountHome'),
    # path('deliveryRequest/',RequestPage.as_view(),name='requestPage'),
    path('pastdeliveries/',pastDeliveries.as_view(),name='pastDeliveries'),
    path('pendingRequest/',pendingRequest.as_view(),name='pendingRequests'),
    path('detailsPage/<int:pk>/',detailsPage.as_view(),name='detailsPage'),
    path('logout/',logoutPage.as_view(),name='logout'),
    path('comingSoon/',comingSoon.as_view(),name='comingSoon'),
    path('bulk/details/<str:unique_id>/',bulkPendingDetails.as_view(),name='bulkPendingDetails'),
    path('requestmod/',requestMod,name='requestPage'),
    path('receipt/<str:unique_id>/',receiptPage,name='receiptPage'),
    path('receiptBulk/<str:unique_id>/',receiptPageBulk,name='receiptPageBulk'),
    path('rulesPolicies/',rulesPolicies,name='rulesPolicies'),
    path('settingsPage/',settingsPage,name='settingsPage'),
    path('quickPlaced/',quickPlaced,name='quickPlaced'),
    path('updateSingle/<str:unique_id>/',update_order_single,name='updateSingle'),
    path('deliveryVal/<str:unique_id>/',deliveryVal,name='deliveryVal'),
    path('bulkDeliveryVal/<str:unique_id>/',bulkDeliveryVal,name='bulkDeliveryVal'),
    path('updateBulk/<str:unique_id>/',update_order_bulk,name='updateBulk'),
]
