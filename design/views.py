from django.shortcuts import render
from .models import Testimonial
from .models import Gallary
# Create your views here.

def index(request):
    testimonials = Testimonial.objects.all()
    pic = Gallary.objects.all()
    return render (request, 'index.html',context={'testimonials': testimonials, 'pic':pic})