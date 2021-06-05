from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DepositViewSet, PortfolioAssetView, PortfolioViewSet, PortfolioParameterViewSet, TradeViewSet, CredentialsViewSet, BotPortfolioList, PortfolioLogEntryViewSet

router = DefaultRouter()
router.register("portfolios", PortfolioViewSet, basename="portfolios")
router.register("portfolio_parameters", PortfolioParameterViewSet,
                basename="portfolio_parameters")
router.register("trades", TradeViewSet, basename="trades")
router.register("deposits", DepositViewSet, basename="deposits")
router.register("portfolio_assets", PortfolioAssetView,
                basename="portfolio_assets")
router.register("portfolio_log", PortfolioLogEntryViewSet,
                basename="portfolio_log")
router.register("credentials", CredentialsViewSet, basename="credentials")

bot_portfolios = [path(
    "api/v1/bot/portfolios", BotPortfolioList.as_view(), name='bot-portfolio-list')]

portfolios_urlpatterns = [
    url("api/v1/", include(router.urls))] + bot_portfolios
