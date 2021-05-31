from django.contrib import admin

# Register your models here.

from .models import Currency, CurrencyStat, CurrencyTag, TagGroup, Tag, Price, MCAPTotal

admin.site.register(Currency)
admin.site.register(TagGroup)
admin.site.register(Tag)
admin.site.register(CurrencyTag)
admin.site.register(Price)
admin.site.register(MCAPTotal)
admin.site.register(CurrencyStat)
