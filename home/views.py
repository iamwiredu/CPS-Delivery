from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .models import Profile
from .forms import ProfileForm
from django.views import View


class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Login(View):

    def get(self, request):
        context = {

        }
        return render(request, 'login.html', context)

    def post(self, request):
        if 'login' in request.POST:
            user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            if user is not None:
                login(request,user)
                print('yes')
                return redirect('/accounthome/')
            
            else:
                print('no')

        context = {
        }
        return render(request, 'home.html', context)
        
class SignUp(View):

    def get(self,request):
        return render(request,'signUp.html')
    
    def post(self, request):

        if 'addUser' in request.POST:
            try:
                username = request.POST.get('username')
                password = request.POST.get('password1')
                email = request.POST.get('email')
                first_name = request.POST.get('fname')
                last_name = request.POST.get('lname')
                phone = request.POST.get('phone')

                # Create the user
                user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                
                # Set the password correctly
                user.set_password(password)
                user.save()

                # Create or get the user's profile
                profile, created = Profile.objects.get_or_create(user=user)
                profile.user = user
                profile.phone = phone  # Assuming `Profile` has a `phone` field
                profile.save()
            except:
                print('error')
            return redirect('/login/')

