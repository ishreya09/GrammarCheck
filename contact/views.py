from django.shortcuts import render
from .models import Contact
from design.models import Testimonial
from design.models import Gallary

# Create your views here.
testimonials = Testimonial.objects.all()
pic = Gallary.objects.all()
def contact(request):
    if request.method == 'POST':
        contact= Contact()
        name= request.POST.get('name', False)
        email= request.POST.get('email',False)
        message= request.POST.get('message',False)
        contact.name, contact.email , contact.message= name, email, message
        contact.save()
        context= {'testimonials':testimonials, 'pic':pic, 'contact': contact}
        return render (request, 'contact_successful.html', context)
    else:
        context= {'testimonials':testimonials, 'pic':pic}
        return render (request, 'index.html', context )
