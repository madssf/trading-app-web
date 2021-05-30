from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DepositViewSet, PortfolioAssetView, PortfolioViewSet, PortfolioParameterViewSet, TradeViewSet, CredentialsViewSet, BotPortfolioList

router = DefaultRouter()
router.register("portfolios", PortfolioViewSet, basename="portfolios")
router.register("portfolio_parameters", PortfolioParameterViewSet,
                basename="portfolio_parameters")
router.register("trades", TradeViewSet, basename="trades")
router.register("deposits", DepositViewSet, basename="deposits")
router.register("portfolio_assets", PortfolioAssetView,
                basename="portfolio_assets")
router.register("credentials", CredentialsViewSet, basename="credentials")

portfolios_urlpatterns = [url("api/v1/", include(router.urls))] + [path(
    "api/v1/bot/portfolios", BotPortfolioList.as_view(), name='bot-portfolio-list')]
