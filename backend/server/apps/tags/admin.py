from django.contrib import admin

# Register your models here.

from .models import TagGroup, Tag

admin.site.register(TagGroup)
admin.site.register(Tag)
