from rest_framework import viewsets

from core.models import Ingredient, Quantity, Recipe, List
from core.serializers import (
    IngredientSerializer,
    QuantitySerializer,
    RecipeSerializer,
    ListSerializer,
)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
