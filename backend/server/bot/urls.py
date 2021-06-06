from .views import CredentialsBotView, CurrencyBotView, ExchangeAssetsBotView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

currencies = [path(
    "api/v1/bot/currencies", csrf_exempt
    (CurrencyBotView.as_view()), name='bot-currencies')]

credentials = [path(
    "api/v1/bot/credentials", CredentialsBotView.as_view(), name='bot-credentials')]

exchange_assets = [path(
    "api/v1/bot/exchange_assets", ExchangeAssetsBotView.as_view(), name='exchange-assets')]

bot_urls = []
bot_urls += currencies
bot_urls += credentials
bot_urls += exchange_assets
