from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLModelViewSet
from apps.endpoints.views import MLModelStatusViewSet
from apps.endpoints.views import MLRequestViewSet
from apps.endpoints.views import PredictView

router = DefaultRouter(trailing_slash=False)

router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlmodels", MLModelViewSet, basename="mlmodels")
router.register(r"mlmodelstatuses", MLModelStatusViewSet, basename="mlmodelstatus")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequest")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    # add predict view url
    path("api/v1/<str:endpoint_name>/predict", PredictView.as_view(), name="predict"),
]