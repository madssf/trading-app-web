from django.contrib import admin

# Register your models here.

from .models import Deposit, Portfolio, PortfolioAsset, PortfolioParameter, Trade, Credentials, PortfolioLogEntry

admin.site.register(Portfolio)
admin.site.register(PortfolioParameter)
admin.site.register(PortfolioAsset)
admin.site.register(Trade)
admin.site.register(Deposit)
admin.site.register(Credentials)
admin.site.register(PortfolioLogEntry)
