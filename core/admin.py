from django.contrib import admin
from .models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    list_filter = ("name", "created_on", "last_modified")
    list_display = ("name", "created_on", "last_modified")


admin.site.register(Ingredient, IngredientAdmin)
