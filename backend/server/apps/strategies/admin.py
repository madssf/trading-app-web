from django.contrib import admin

# Register your models here.

from .models import Strategy, ParameterType, Parameter, StrategyParameter

admin.site.register(Strategy)
admin.site.register(ParameterType)
admin.site.register(Parameter)
admin.site.register(StrategyParameter)
