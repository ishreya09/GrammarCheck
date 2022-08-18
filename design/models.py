from django.db import models

# Create your models here.

class Testimonial (models.Model):
    name = models.CharField(max_length=500)
    img = models.ImageField(upload_to = 'pics')
    review = models.TextField()
    designation = models.CharField(max_length=200)

class Gallary (models.Model):
    img = models.ImageField(upload_to = 'gallary')
    desc =models.CharField(max_length=500) #description of images
    subdesc = models.CharField(max_length=500) #sub description of images