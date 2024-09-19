from django.urls import path
from .views import Home, Login, SignUp


urlpatterns = [
    path('',Home.as_view(),name='homepage'),
    path('login/',Login.as_view(),name='loginPage'),
    path('signUp/',SignUp.as_view(),name='signupPage')
]