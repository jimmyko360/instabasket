from rest_framework import serializers
from core.models import Ingredient, Quantity, Recipe, List

# from django.contrib.auth.models import User


class IngredientSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")

    # reverse relationship with Quantity model
    quantities = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    created_on = serializers.DateTimeField(read_only=True)
    last_modified = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        user_timezone = self.get_user_timezone()
        created_on = instance.created_on.astimezone(user_timezone)
        last_modified = instance.last_modified.astimezone(user_timezone)
        representation = super().to_representation(instance)
        representation["created_on"] = created_on.strftime("%x %X %Z")
        representation["last_modified"] = last_modified.strftime("%x %X %Z")

        return representation

    def get_user_timezone(self):
        user_timezone = (
            self.context["request"].user.tzinfo if "request" in self.context else None
        )
        return user_timezone

    class Meta:
        model = Ingredient
        fields = ["id", "name", "created_on", "last_modified", "quantities"]


class QuantitySerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")

    # reverse relationship with Recipe model
    recipes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # reverse relationship with List model
    lists = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    created_on = serializers.DateTimeField(read_only=True)
    last_modified = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        user_timezone = self.get_user_timezone()
        created_on = instance.created_on.astimezone(user_timezone)
        last_modified = instance.last_modified.astimezone(user_timezone)
        representation = super().to_representation(instance)
        representation["created_on"] = created_on.strftime("%x %X %Z")
        representation["last_modified"] = last_modified.strftime("%x %X %Z")

        return representation

    def get_user_timezone(self):
        user_timezone = (
            self.context["request"].user.tzinfo if "request" in self.context else None
        )
        return user_timezone

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


class RecipeSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")

    # reverse relationship with List model
    lists = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    created_on = serializers.DateTimeField(read_only=True)
    last_modified = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        user_timezone = self.get_user_timezone()
        created_on = instance.created_on.astimezone(user_timezone)
        last_modified = instance.last_modified.astimezone(user_timezone)
        representation = super().to_representation(instance)
        representation["created_on"] = created_on.strftime("%x %X %Z")
        representation["last_modified"] = last_modified.strftime("%x %X %Z")

        return representation

    def get_user_timezone(self):
        user_timezone = (
            self.context["request"].user.tzinfo if "request" in self.context else None
        )
        return user_timezone

    class Meta:
        model = Recipe
        fields = ["id", "name", "ingredients", "created_on", "last_modified", "lists"]


class ListSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")

    created_on = serializers.DateTimeField(read_only=True)
    last_modified = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        user_timezone = self.get_user_timezone()
        created_on = instance.created_on.astimezone(user_timezone)
        last_modified = instance.last_modified.astimezone(user_timezone)
        representation = super().to_representation(instance)
        representation["created_on"] = created_on.strftime("%x %X %Z")
        representation["last_modified"] = last_modified.strftime("%x %X %Z")

        return representation

    def get_user_timezone(self):
        user_timezone = (
            self.context["request"].user.tzinfo if "request" in self.context else None
        )
        return user_timezone

    class Meta:
        model = List
        fields = [
            "id",
            "title",
            "recipes",
            "ingredients",
            "created_on",
            "last_modified",
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
