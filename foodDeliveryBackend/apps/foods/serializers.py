from rest_framework import serializers
from .models import Food, FoodCategory


class FoodCategorySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return FoodCategory.objects.create(**validated_data)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name')


class FoodSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Food.objects.create(**validated_data)

    class Meta:
        model = Food
        fields = ('id', 'name', 'description', 'price',
                  'active', 'is_veg', 'quantity')
