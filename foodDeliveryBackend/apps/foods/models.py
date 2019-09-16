from django.db import models
from django.contrib.postgres.fields import JSONField

from apps.restaurants.models import Restaurant


class FoodCategory(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(
        Restaurant, related_name="categories", on_delete=models.CASCADE)


class Food(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        FoodCategory, related_name="foods", on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurant, related_name="foods", on_delete=models.CASCADE)
    description = models.TextField()
    active = models.BooleanField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_veg = models.BooleanField()
    quantity = JSONField(default=dict)
