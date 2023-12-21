from django.contrib import admin
from .models import Ingredient, Quantity, Recipe


class IngredientAdmin(admin.ModelAdmin):
    list_filter = ("name", "created_on", "last_modified")
    list_display = ("name", "created_on", "last_modified")


class QuantityAdmin(admin.ModelAdmin):
    list_filter = (
        "ingredient",
        "quantity",
        "unit",
        "system",
        "attribute",
        "conversion_multiple",
        "created_on",
        "last_modified",
    )
    list_display = (
        "ingredient",
        "quantity",
        "unit",
        "system",
        "attribute",
        "conversion_multiple",
        "created_on",
        "last_modified",
    )


class RecipeAdmin(admin.ModelAdmin):
    list_filter = (
        "name",
        "ingredients",
        "created_on",
        "last_modified",
    )
    list_display = (
        "name",
        "created_on",
        "last_modified",
    )


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Quantity, QuantityAdmin)
admin.site.register(Recipe, RecipeAdmin)
