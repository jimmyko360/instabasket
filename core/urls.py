from django.urls import path, include
from core.views import IngredientViewSet, QuantityViewSet, RecipeViewSet, ListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"ingredients", IngredientViewSet, basename="ingredient")
router.register(r"quantity", QuantityViewSet, basename="quantity")
router.register(r"recipes", RecipeViewSet, basename="recipe")
router.register(r"lists", ListViewSet, basename="list")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
