from django.conf import settings
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet

app_name = "api"

router_v1 = SimpleRouter()
router_v1.register("posts", PostViewSet, basename="posts")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
