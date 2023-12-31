from rest_framework import serializers
from core.models import Ingredient, Quantity, Recipe, List

# from django.contrib.auth.models import User

# used to create a placeholder timezone that should be received from the frontend
import pytz


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")

    quantities = serializers.HyperlinkedRelatedField(
        many=True, view_name="quantity-detail", read_only=True
    )

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
        # user_timezone = (
        #     self.context["request"].user.tzinfo
        #     if self.context["request"] and self.context["request"].user.tzinfo
        #     else None
        # )

        # return user_timezone

        return pytz.timezone("America/New_York")

    class Meta:
        model = Ingredient
        fields = ["url", "id", "name", "created_on", "last_modified", "quantities"]


class QuantitySerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")

    recipes = serializers.HyperlinkedRelatedField(
        many=True, view_name="recipe-detail", read_only=True
    )

    lists = serializers.HyperlinkedRelatedField(
        many=True, view_name="list-detail", read_only=True
    )

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
        # user_timezone = (
        #     self.context["request"].user.tzinfo
        #     if self.context["request"] and self.context["request"].user.tzinfo
        #     else None
        # )

        # return user_timezone

        return pytz.timezone("America/New_York")

    class Meta:
        model = Quantity
        fields = [
            "url",
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


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")

    lists = serializers.HyperlinkedRelatedField(
        many=True, view_name="list-detail", read_only=True
    )

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
        # user_timezone = (
        #     self.context["request"].user.tzinfo
        #     if self.context["request"] and self.context["request"].user.tzinfo
        #     else None
        # )

        # return user_timezone

        return pytz.timezone("America/New_York")

    class Meta:
        model = Recipe
        fields = [
            "url",
            "id",
            "name",
            "ingredients",
            "created_on",
            "last_modified",
            "lists",
        ]


class ListSerializer(serializers.HyperlinkedModelSerializer):
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
        # user_timezone = (
        #     self.context["request"].user.tzinfo
        #     if self.context["request"] and self.context["request"].user.tzinfo
        #     else None
        # )

        # return user_timezone

        return pytz.timezone("America/New_York")

    class Meta:
        model = List
        fields = [
            "url",
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
