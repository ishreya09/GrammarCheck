from django.shortcuts import render
from django.shortcuts import redirect
from .models import SubscribeModel
from django.contrib import messages
from design.models import Testimonial
from design.models import Gallary
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token
from newsletter.tokens import unsubscibe_token
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import View
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from django.core.mail import send_mail  
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from accounts.models import Profile


# Create your views here.
testimonials = Testimonial.objects.all()
pic = Gallary.objects.all()
profile = Profile.objects.all()

# Create your views here.
def subscribe(request):
    if request.method =='POST':
        subscribemodel= SubscribeModel()
        username=request.POST.get("username", False)
        
        user = User.objects.get(username=username)
        profile= Profile.objects.get(user_id= user.id)
        current_site = get_current_site(request)
        subscribemodel.name , subscribemodel.email= user.first_name, user.email
        
        
        if SubscribeModel.objects.filter(email= user.email).exists():
            messages.error(request, "The email already exists")
            return redirect('/')
        else:
            user.profile.newsletter = True
            subscribemodel.save()
            messages.success (request, "email added to newsletters")
            
            return render(request, "newsletter_subscribe.html", context= {'subscribemodel' : subscribemodel, 'testimonials':testimonials, 'pic':pic,'user': user,'domain': current_site.domain,'uid': urlsafe_base64_encode(force_bytes(user.pk)),'token': unsubscibe_token.make_token(user)})
            
    else:
        return render(request, "index.html", context= {'testimonials':testimonials, 'pic':pic})


from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core import mail
from .models import NewsletterEmail
from Grammarly import settings
from django.template.loader import render_to_string

from django.contrib.admin.views.decorators import staff_member_required

from .forms import NewsletterEmailForm


def mail(request):
    form= NewsletterEmailForm(request.POST, request.FILES)
    if request.method =='POST':
        if form.is_valid():
            instance1= form.save()
            subscriber=SubscribeModel.objects.all()
            

            profile = Profile.objects.all()
            emails=[]
            emails = SubscribeModel.objects.all().values_list('email', flat=True)
            print (emails)
            
        
            for email in emails:
                current_site = get_current_site(request)
                user = User.objects.get (email = email)
    
        
                html_message = render_to_string('newsletter_email.html', {'newsletter': instance1,'subscriber':subscriber,'user': user,'domain': current_site.domain,'uid': urlsafe_base64_encode(force_bytes(user.pk)),'token': unsubscibe_token.make_token(user)})
                from_email = settings.EMAIL_HOST_USER
                msg= EmailMessage(subject= instance1.subject, from_email=from_email , bcc= [email,], body=html_message)
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()

            return render (request, 'newsletter-sent.html', context= {'testimonials':testimonials, 'pic':pic,'user': user,'domain': current_site.domain,'uid': urlsafe_base64_encode(force_bytes(user.pk)),'token': unsubscibe_token.make_token(user)})
        else:
            messages.warning = (request, "Please fill the details properly")
            return render(request, 'create_newsletter.html',context= {'form':form,'testimonials':testimonials, 'pic':pic})
    else:
        return render(request, 'create_newsletter.html',context= {'form':form,'testimonials':testimonials, 'pic':pic})



class Unsubscribe(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if (user is not None and unsubscibe_token.check_token(user, token) or (request.user.is_authenticated() and request.user == user)):
            profile= Profile.objects.get(user_id= user.id)
            user.profile.newsletter = False
            SubscribeModel.objects.filter(email= user.email).delete()
            messages.success(request, "You email has been Unsubscribed")
            return render(request, 'unsubscribe.html')
        else:
            messages.error("Login is required to unsubscribe")
            return redirect("/")
        
'''
def unsubscribe(request):
    subscribemodel= SubscribeModel()
    email=request.POST.get("name", False)
    if SubscribeModel.objects.filter(email= email).exists():
        SubscribeModel.objects.filter(email= email).delete()
        messages.success(request, "You email has been Unsubscribed")
    else:
        messages.warning(request, "Sorry! We cannot find your email address in our database!")

from django.core.signing import TimestampSigner, BadSignature, SignatureExpired

def create_unsubscribe_link(self):
    username, token = self.make_token().split(":", 1)
    return reverse('newsletter.views.unsubscribe',
                   kwargs={'username': username, 'token': token,})

def make_token(self):
    return TimestampSigner().sign(self.user.username)

def check_token(self, token):
    try:
        key = '%s:%s' % (self.user.username, token)
        TimestampSigner().unsign(key, max_age=60 * 60 * 48) # Valid for 2 days
    except (BadSignature, SignatureExpired):
        return False
    return True

def unsubscribe(request, username, token):
    """ 
    User is immediately unsubscribed if they are logged in as username, or
    if they came from an unexpired unsubscribe link. Otherwise, they are
    redirected to the login page and unsubscribed as soon as they log in.
    """

    user = get_object_or_404(User, username=username, is_active=True)

    if ( (request.user.is_authenticated() and request.user == user) or
         user.get_profile().check_token(token)):
       # unsubscribe them
       profile = user.get_profile()
       SubscribeModel.objects.filter(email= profile.email).delete()
       messages.success(request, "You email has been Unsubscribed")
       return render(request, 'unsubscribe.html')
    
    # Otherwise redirect to login page
    next_url = reverse('newsletter.views.unsubscribe', 
                       kwargs={'username': username, 'token': token,})
    return HttpResponseRedirect('%s?next=%s' % (reverse('login'), next_url))
'''






