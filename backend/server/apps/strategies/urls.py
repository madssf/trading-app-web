from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import StrategyViewSet, ParameterTypeViewSet, ParameterViewSet, StrategyParameterViewSet

router = DefaultRouter()
router.register("strategies", StrategyViewSet, basename="strategies")
router.register("parameter_types", ParameterTypeViewSet,
                basename="parameter_types")
router.register("parameters", ParameterViewSet,
                basename="parameters")
router.register("strategy_parameters", StrategyParameterViewSet,
                basename="strategy_parameters")

strategies_urlpatterns = [url("api/v1/", include(router.urls))]
