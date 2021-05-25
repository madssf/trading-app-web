from django.contrib import admin

# Register your models here.

from .models import Currency, CurrencyTag, TagGroup, Tag, Price

admin.site.register(Currency)
admin.site.register(TagGroup)
admin.site.register(Tag)
admin.site.register(CurrencyTag)
admin.site.register(Price)
