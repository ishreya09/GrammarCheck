from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    bio= models.CharField(max_length=500,null=True, blank= True)
    mobilenumber = models.CharField(null=True, blank=True, max_length=15)
    Profile_pic = models.ImageField(upload_to='user_dp', default= "user_dp/default.png",null=True, blank=True)
    Date_of_birth= models.DateField(null=True, blank=True)
    Country = models.CharField(max_length=30,null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    newsletter= models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()