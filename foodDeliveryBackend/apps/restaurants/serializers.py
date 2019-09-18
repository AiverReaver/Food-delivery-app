from rest_framework import serializers
from .models import Restaurant
from apps.foods.serializers import FoodCategorySerializer
from apps.foods.models import FoodCategory


class RestaurantSerializer(serializers.ModelSerializer):

    categories = FoodCategorySerializer(many=True, read_only=True)

    def __init__(self, *args, **kwargs):
        # initialize fields
        fields = kwargs.pop('fields', None)
        super(RestaurantSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'categories')
