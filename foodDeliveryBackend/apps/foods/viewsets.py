from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Food, FoodCategory
from apps.restaurants.models import Restaurant
from .serializers import FoodSerializer, FoodCategorySerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

    def create(self, request, restaurant_pk=None, *args, **kwargs):

        if not request.user.is_restaurant:
            return Response({'message': 'unauthorized'}, 401)

        serializer = FoodCategorySerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        if restaurant_pk is None:
            return Response({'message': 'restaurant required'})

        restaurant = Restaurant.objects.get(pk=restaurant_pk)

        serializer.save(restaurant=restaurant)

        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def list(self, request, category_pk=None, restaurant_pk=None):
        if category_pk is not None and restaurant_pk is not None:
            queryset = Food.objects.filter(
                category_id=category_pk, restaurant_id=restaurant_pk)
        elif restaurant_pk is not None and category_pk is None:
            queryset = Food.objects.filter(restaurant_id=restaurant_pk)
        else:
            queryset = Food.objects.filter(category_id=category_pk)

        serializer = FoodSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, restaurant_pk=None, category_pk=None, *args, **kwargs):

        if not request.user.is_restaurant:
            return Response({'message': 'unauthorized'}, 401)

        serializer = FoodSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        foodCategory = FoodCategory.objects.get(
            pk=category_pk)
        restaurant = Restaurant.objects.get(
            pk=restaurant_pk)
        serializer.save(category=foodCategory, restaurant=restaurant)

        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
