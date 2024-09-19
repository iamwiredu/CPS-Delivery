from django.urls import path
from .views import accountHome, RequestPage,pastDeliveries, pendingRequest, detailsPage

urlpatterns = [
    path('accounthome/',accountHome.as_view(),name='accountHome'),
    path('deliveryRequest/',RequestPage.as_view(),name='requestPage'),
    path('pastdeliveries/',pastDeliveries.as_view(),name='pastDeliveries'),
    path('pendingRequest',pendingRequest.as_view(),name='pendingRequests'),
     path('detailsPage/<int:pk>/',detailsPage.as_view(),name='detailsPage'),
]