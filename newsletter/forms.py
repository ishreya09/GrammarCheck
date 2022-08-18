from .models import NewsletterEmail
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

class NewsletterEmailForm(forms.ModelForm):
    subject=forms.CharField(max_length= 500,label="Subject of email", required= True )
    subheading=forms.CharField(max_length= 500, label="Sub-heading", required= False)
    img = forms.ImageField(required= False, label="Image to be added in the Email")
    post = forms.CharField(required= True, label= "Body of Email", widget=forms.Textarea())
    class Meta:
        model= NewsletterEmail
        fields= ('subject', 'subheading','img','post',)
