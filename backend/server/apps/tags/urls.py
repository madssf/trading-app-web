from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import TagGroupViewSet, TagViewSet

router = DefaultRouter()
router.register("tag_groups", TagGroupViewSet, basename="tag_groups")
router.register("tags", TagViewSet, basename="tag")

tags_urlpatterns = [url("api/v1/", include(router.urls))]
