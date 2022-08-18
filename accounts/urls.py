from django.urls import path
from accounts.views import ActivateAccount
from . import views
from accounts.views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('login', views.login  , name= "login"),
    path('savelogin', views.login , name= "savelogin"),
    path('logout', views.logout, name="logout"),
    path('profile', views.profile, name= 'profile'),
    path('updateprofile', views.updateprofile , name= 'updateprofile'),
    path('saveprofile', views.updateprofile , name= "savefrofile"),
   # Change Password
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change-password.html',
            success_url = '/') ,  name='change_password'),
    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password-reset.html',
             subject_template_name='password_reset_subject.txt',
             email_template_name='password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password-reset-done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
       
