from django.urls import path
from .views import restaurantHome, restaurantSignUp, restaurantAdmin, restaurantUpdate, restaurantFood, restaurantOrder, cart_view, add_to_cart


urlpatterns = [
    path('restaurant/home',restaurantHome.as_view(),name='restaurantHome'),
    path('restaurantSignUp/',restaurantSignUp.as_view(),name='restaurantSignUp'),
    path('restaurantAdmin/',restaurantAdmin.as_view(),name='restaurantAdmin'),
    path('restaurantUpdate/<str:unique_id>/',restaurantUpdate.as_view(),name='restaurantUpdate'),
    path('restaurantFood/<str:unique_id>/',restaurantFood.as_view(),name='restaurantFood'),
    path('restaurantOrder/<str:unique_id>/',restaurantOrder.as_view(),name='restaurantOrder'),
    path('cart/', cart_view, name='cart_view'),               # View the cart
    path('cart/add/<int:food_id>/', add_to_cart, name='add_to_cart'),   # Add food to cart
]