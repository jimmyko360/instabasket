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


class QuantityViewSet(viewsets.ModelViewSet):
    queryset = Quantity.objects.all()
    serializer_class = QuantitySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
