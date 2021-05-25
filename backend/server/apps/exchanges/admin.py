from django.contrib import admin

# Register your models here.

from .models import Credentials, Exchange

admin.site.register(Exchange)
admin.site.register(Credentials)
