from django.db import models

# Create your models here.
class SubscribeModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    name = models.CharField(max_length=500)
    email= models.EmailField()
    status = models.BooleanField(null=False, blank=True, default=False)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.email




class NewsletterEmail(models.Model):
    subject=models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add= True)
    subheading= models.CharField(max_length=500, null = True , blank= True)
    post = models.TextField( null = True , blank= True)
    img = models.ImageField(upload_to= 'newsletter', null = True , blank= True)
    def get_subject(self):
        return self.subject
    