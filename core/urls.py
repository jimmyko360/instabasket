from django.urls import path, include
from core.views import (
    UserViewSet,
    IngredientViewSet,
    QuantityViewSet,
    RecipeViewSet,
    ListViewSet,
)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"ingredients", IngredientViewSet, basename="ingredient")
router.register(r"quantity", QuantityViewSet, basename="quantity")
router.register(r"recipes", RecipeViewSet, basename="recipe")
router.register(r"lists", ListViewSet, basename="list")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", views.obtain_auth_token),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
]
