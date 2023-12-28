from rest_framework import serializers
from core.models import Ingredient, Quantity, Recipe, List

# from django.contrib.auth.models import User


class IngredientSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")

    # reverse relationship with Quantity model
    quantities = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # come back to this later:
    # created_on = serializers.DateTimeField(format="%x %X", read_only=True)
    # last_modified = serializers.DateTimeField(format="%x %X", read_only=True)

    class Meta:
        model = Ingredient
        fields = ["id", "name", "created_on", "last_modified", "quantities"]


class QuantitySerializer(serializers.ModelSerializer):
    # reverse relationship with Recipe model
    recipes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # reverse relationship with List model
    lists = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # set created_on and last_modified as read_only

    class Meta:
        model = Quantity
        fields = [
            "id",
            "ingredient",
            "quantity",
            "unit",
            "system",
            "attribute",
            "conversion_multiple",
            "created_on",
            "last_modified",
            "recipes",
            "lists",
        ]


"""
Implement this later

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name="snippet-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]
"""
