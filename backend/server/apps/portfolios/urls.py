from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet, PortfolioParameterViewSet

router = DefaultRouter()
router.register("portfolios", PortfolioViewSet, basename="portfolios")
router.register("portfolio_parameters", PortfolioParameterViewSet,
                basename="portfolio_parameters")

portfolios_urlpatterns = [url("api/v1/", include(router.urls))]
