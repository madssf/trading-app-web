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
from apps.users.urls import users_urlpatterns
from apps.exchanges.urls import exchanges_urlpatterns
from apps.strategies.urls import strategies_urlpatterns
from apps.portfolios.urls import portfolios_urlpatterns
from apps.currencies.urls import currencies_urlpatterns
from apps.watchlists.urls import watchlists_urlpatterns
from pages.urls import pages_urlpatterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += users_urlpatterns
urlpatterns += exchanges_urlpatterns
urlpatterns += strategies_urlpatterns
urlpatterns += portfolios_urlpatterns
urlpatterns += currencies_urlpatterns
urlpatterns += watchlists_urlpatterns
urlpatterns += pages_urlpatterns
urlpatterns += staticfiles_urlpatterns()
