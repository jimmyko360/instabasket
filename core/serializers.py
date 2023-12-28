from rest_framework import serializers
from core.models import Ingredient, Quantity, Recipe, List

# from django.contrib.auth.models import User


class IngredientSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")
    quantities = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Quantity.objects.all(), required=False
    )
    # created_on = serializers.DateTimeField(format="%x %X", read_only=True)
    # last_modified = serializers.DateTimeField(format="%x %X", read_only=True)
    # come back to this later

    class Meta:
        model = Ingredient
        fields = ["id", "name", "created_on", "last_modified", "quantities"]


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
