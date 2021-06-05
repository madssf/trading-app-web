"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.users.urls import users_urls
from apps.exchanges.urls import exchanges_urls
from apps.strategies.urls import strategies_urls
from apps.portfolios.urls import portfolios_urls
from apps.currencies.urls import currencies_urls
from apps.watchlists.urls import watchlists_urls
from pages.urls import pages_urls
from bot.urls import bot_urls

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += users_urls
urlpatterns += exchanges_urls
urlpatterns += strategies_urls
urlpatterns += portfolios_urls
urlpatterns += currencies_urls
urlpatterns += watchlists_urls
urlpatterns += pages_urls
urlpatterns += bot_urls
urlpatterns += staticfiles_urlpatterns()
