from .views import CurrencyBatchView, PortfolioCredentials
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

batch_update_currencies = [path(
    "api/v1/bot/currencies", csrf_exempt
    (CurrencyBatchView.as_view()), name='bot-currencies')]

portfolio_credentials = [path(
    "api/v1/bot/credentials", PortfolioCredentials.as_view(), name='bot-credentials')]


bot_urls = []
bot_urls += batch_update_currencies
bot_urls += portfolio_credentials
