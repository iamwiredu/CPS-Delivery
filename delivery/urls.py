from django.urls import path
from .views import accountHome, requestMod, receiptPage,bulkPendingDetails,comingSoon,logoutPage,RequestPage,pastDeliveries, pendingRequest, detailsPage

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
]
