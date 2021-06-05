from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from .views import *

pages_urls = [
    path('', TemplateView.as_view(template_name='home.html'), name="home"),
    path('my_portfolios/',
         MyPortfoliosView, name="my_portfolios"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('my_portfolios/<int:id>', PortfolioID, name='portfolioid')

]
