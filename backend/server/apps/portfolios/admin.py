from django.contrib import admin

# Register your models here.

from .models import Portfolio, PortfolioParameter

admin.site.register(Portfolio)
admin.site.register(PortfolioParameter)
