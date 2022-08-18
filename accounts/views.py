from django.shortcuts import render
from design.models import Testimonial
from design.models import Gallary
from .models import Profile
from accounts.forms import ProfileForm
from accounts.forms import UserForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.urls import reverse
from django.http import HttpResponse  
from Grammarly import settings  
from django.urls import reverse
# Create your views here.

testimonials = Testimonial.objects.all()
pic = Gallary.objects.all()

from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import View
from accounts.forms import SignUpForm
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token
from django.core.mail import send_mail  
from newsletter.models import SubscribeModel

# Sign Up View
class SignUpView(View):
    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'signup.html' , {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False # Deactivate account till it is confirmed
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Grammar Check Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, ('Your Registration form is submitted, Please Confirm your email to complete registration.'))

            return redirect('login')
        messages.error(request, 'Form submitted is not valid or does not provide imformation for the required fields')
        form = self.form_class()
        return render(request, 'signup.html' , {'form': form})

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from accounts.tokens import account_activation_token

class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            auth.login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('/')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('/')



def updateprofile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            a= user_form.save()
            b= profile_form.save()
            user= User.objects.get(email= a.email)
            profile= Profile.objects.get(user_id=a.id)
            if user.profile.newsletter==True:
                s = SubscribeModel()
                s.name,s.email= user.first_name ,user.email
                if SubscribeModel.objects.filter(email= user.email).exists():
                    messages.error(request, "The email already exists in newsletter")
                    return redirect('/profile')
                else:
                
                    s.save()
                    messages.success (request, "email added to newsletters")
            

            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please provide valid details.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'editprofile.html', {
        'user_form': user_form,
        'profile_form': profile_form
        })

def login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username',False)
        password = request.POST.get('password',False)
        
        user = auth.authenticate(username=username, password= password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in successfully')
            return redirect('/')
        else:
            messages.error(request, 'invalid username or password')
            return redirect ('login')

    elif request.method == 'GET':
        return render(request, 'login.html',context={'testimonials': testimonials, 'pic':pic})

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    profile = Profile.objects.all()
    return render(request, 'profile.html', context={'testimonials': testimonials, 'pic':pic, 'profile':profile})

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False