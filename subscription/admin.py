#*-* coding: utf-8 *-*
from django.contrib import admin
from django.db import models
from subscription.models import Subscription 

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "cpf", "created_at"]
    list_filter = ["created_at"]
    
    search_fields = ["name"]
    
admin.site.register(Subscription, SubscriptionAdmin)