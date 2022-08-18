from django.urls import path
from . import views
from .views import Unsubscribe

urlpatterns = [
    path('subscribe', views.subscribe  , name= "subscribe"),
    path('unsubscribe/<uidb64>/<token>/', Unsubscribe.as_view(), name='unsubscribe'),
    path('createnewsletter', views.mail, name= "createnewsletter"),
    path('sendnewsletter', views.mail, name= "sendnewsletter"),
]