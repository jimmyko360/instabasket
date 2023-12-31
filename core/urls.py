from django.urls import path, include
from core.views import IngredientViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"ingredients", IngredientViewSet, basename="ingredient")

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
