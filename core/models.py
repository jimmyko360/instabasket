from django.db import models

# these lines are taken directly from the DRF docs
# they automatically generate a Token for newly created Users
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# used for automatically assigning measurement system and unit fields on the Quantity model
us_volume_choices = ["tsp", "Tbsp", "fl oz", "cp", "pt", "qt", "gal"]
metric_volume_choices = ["ml", "l"]

us_weight_choices = ["oz", "lb"]
metric_weight_choices = ["mg", "g", "kg"]


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        "auth.User", related_name="ingredients", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_on"]


class Quantity(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="quantities"
    )
    quantity = models.DecimalField(max_digits=6, decimal_places=3)
    unit = models.CharField(
        max_length=5,
        choices=[
            (x, x)
            for x in [
                *us_volume_choices,
                *metric_volume_choices,
                *us_weight_choices,
                *metric_weight_choices,
            ]
        ],
    )
    system = models.CharField(
        max_length=6, choices=[("us", "us"), ("metric", "metric")], editable=False
    )
    attribute = models.CharField(
        max_length=6,
        choices=[("volume", "volume"), ("weight", "weight")],
        editable=False,
    )
    conversion_multiple = models.DecimalField(max_digits=13, decimal_places=3)
    # conversion_multiple should also have the editable=False option after once a calculation process is implemented
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        "auth.User", related_name="quantities", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.ingredient.name}"

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Quantities"

    def save(self, *args, **kwargs):
        if self.unit in metric_volume_choices:
            self.system = "metric"
            self.attribute = "volume"
        elif self.unit in metric_weight_choices:
            self.system = "metric"
            self.attribute = "weight"
        elif self.unit in us_weight_choices:
            self.system = "us"
            self.attribute = "weight"
        else:
            self.system = "us"
            self.attribute = "volume"

        super().save(*args, **kwargs)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Quantity, related_name="recipes")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        "auth.User", related_name="recipes", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_on"]


class List(models.Model):
    title = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe, blank=True, related_name="lists")
    ingredients = models.ManyToManyField(Quantity, blank=True, related_name="lists")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        "auth.User", related_name="lists", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]
