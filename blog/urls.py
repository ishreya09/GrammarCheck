from django.urls import path

from django.urls import include
from . import views
# importing django routing libraries
from .views import postdetail
from .views import PostListView

urlpatterns = [
    # home page
    path('', PostListView.as_view() , name='post_list'),
    path('<slug:slug>', postdetail.as_view(), name='post_detail'),

]