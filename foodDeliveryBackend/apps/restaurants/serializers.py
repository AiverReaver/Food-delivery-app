from rest_framework import serializers
from .models import Restaurant
from apps.foods.serializers import FoodCategorySerializer


class RestaurantSerializer(serializers.ModelSerializer):

    categories = FoodCategorySerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'categories', ]
