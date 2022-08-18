from django.contrib import admin
from .models import SubscribeModel
from .models import NewsletterEmail
# Register your models here.

class SubscribeAdmin(admin.ModelAdmin):
    list_display= ('name','email','status','created_date','updated_date',)

admin.site.register(SubscribeModel, SubscribeAdmin)
admin.site.register(NewsletterEmail)
