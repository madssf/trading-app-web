from django.contrib import admin

# Register your models here.

from .models import Watchlist, WatchlistCurrency

admin.site.register(Watchlist)
admin.site.register(WatchlistCurrency)
