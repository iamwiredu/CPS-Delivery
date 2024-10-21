from django.shortcuts import render, redirect
from django.middleware.csrf import CsrfViewMiddleware
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .models import Profile
from .forms import ProfileForm
from rider.views import riderManagement
from restaurant.views import restaurantAdmin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

class Home(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        return render(request,'home.html')

class Login(View):


    def get(self, request):
        all_messages = messages.get_messages(request)
        first_message = None
        if all_messages:
            first_message = list(all_messages)[0]
        context = {
            'first_message' : first_message,
        }
        return render(request, 'login.html', context)

    def post(self, request):
        if 'login' in request.POST:
            try:
                user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
                if user is not None:
                    login(request,user)
                    print('yes')
                    if user.is_superuser:
                        return redirect('/adminConsole/')
                    elif user.profile.accountType == 'Rider':
                        return redirect(riderManagement,request.user.profile.rider.unique_id) # associate every rider profile with a rider object
                    elif user.profile.accountType == 'Restaurant':
                        return redirect('/restaurantAdmin/')
                    else:
                        print(user.profile.accountType)
                        return redirect('/accounthome/')
                else:
                    messages.error(request,'Wrong Password or Username.')
                    return redirect('/login/')
            except:
                messages.error(request,'Error logging in.')
                return redirect('/login/')
                   

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
                password2 = request.POST.get('password2')
                first_name = request.POST.get('fname')
                last_name = request.POST.get('lname')
                phone = request.POST.get('phone')

                error_messages = []

                # Check if passwords match
                if password != password2:
                    error_messages.append('Passwords do not match.')

                # Check if the username already exists
                if User.objects.filter(username=username).exists():
                    error_messages.append('Username has already been taken.')



                # If there are any errors, add them to messages and redirect once
                if error_messages:
                    for error in error_messages:
                        messages.error(request, error)
                    return redirect('/signUp/')


                # Create the user
                user = User.objects.create(username=username, first_name=first_name, last_name=last_name)
                
                # Set the password correctly
                user.set_password(password)
                user.save()

                # Create or get the user's profile
                profile, created = Profile.objects.get_or_create(user=user)
                profile.user = user
                profile.phone = phone  # Assuming `Profile` has a `phone` field
                profile.accountType = 'Nuser'
                profile.save()
            except CsrfViewMiddleware as csrf_error:
                messages.error(request, 'Error. Please refresh the page and try again.')
                return redirect('/signUp/') 
            except Exception as e:
                messages.error(request,e)
                return redirect('/signUp/')
            messages.success(request,'account created!')
            return redirect('/login/')


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def settings(request):
    PasswordChangeFormCreator = PasswordChangeForm(request.user)
    all_messages = messages.get_messages(request)
    first_message = None
    if all_messages:
        first_message = list(all_messages)[0]


    if 'changePassword' in request.POST:
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,'You successfully changed your password!')
            return redirect('/settings/')
        else:
            messages.error(request,'Error changing Password.')
            return redirect('/settings/')
            
    context = {
        'PasswordChangeFormCreator':PasswordChangeFormCreator,
        'first_message':first_message,
    }
    return render(request,'settings.html',context)