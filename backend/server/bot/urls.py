from .views import CredentialsBotView, CurrencyBotView, ExchangeAssetsBotView, StrategyInstructionsView, StrategyPortfoliosBotView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

currencies = [path(
    "api/v1/bot/currencies", csrf_exempt
    (CurrencyBotView.as_view()), name='bot-currencies')]

credentials = [path(
    "api/v1/bot/credentials", CredentialsBotView.as_view(), name='bot-credentials')]

exchange_assets = [path(
    "api/v1/bot/exchange_assets", ExchangeAssetsBotView.as_view(), name='exchange-assets')]

strategy_portfolios = [path(
    "api/v1/bot/strategy_portfolios", StrategyPortfoliosBotView.as_view(), name='strategy-portfolios')]

strategy_instructions = [path(
    "api/v1/bot/strategy_instructions", StrategyInstructionsView.as_view(), name='strategy-instructions')]


bot_urls = []
bot_urls += currencies
bot_urls += credentials
bot_urls += exchange_assets
bot_urls += strategy_portfolios
bot_urls += strategy_instructions
