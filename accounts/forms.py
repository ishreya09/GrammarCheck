from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import datetime
# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    Date_of_birth= forms.DateField(required=False ,help_text = "Please use the following format: <em>YYYY-MM-DD</em>." ,widget=forms.SelectDateWidget(empty_label=("choose year","choose month", "choose date"),years=range(datetime.date.today().year-100, datetime.date.today().year +1 )))
    mobilenumber=forms.CharField(required= False, help_text ="Enter your mobile no along with your country code")
    class Meta:
        model = Profile
        fields = ('bio', 'mobilenumber','Profile_pic', 'Date_of_birth', 'Country','newsletter',)