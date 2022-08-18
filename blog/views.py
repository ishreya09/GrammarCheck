from django.shortcuts import render
from design.models import Testimonial
from design.models import Gallary
from .models import Blogger
# importing models and libraries
from django.views.generic import ListView 
from django.views.generic import DetailView
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

testimonials = Testimonial.objects.all()
pic = Gallary.objects.all()


# class based views for posts

class PostListView(ListView):
    
    model = Blogger
    template_name = 'post.html'

class postdetail(DetailView):
    
    model = Blogger
    template_name = "post_detail.html"
    
