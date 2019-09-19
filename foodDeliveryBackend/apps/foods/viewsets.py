from rest_framework import viewsets
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

    def create(self, request, restaurant_pk=None, *args, **kwargs):

        if not request.user.is_restaurant:
            return Response({'message': 'unauthorized'}, 401)

        serializer = FoodSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        if not 'category' in request.data:
            return Response({'message': 'category required'})

        if restaurant_pk is None:
            return Response({'message': 'restaurant required'})

        foodCategory = FoodCategory.objects.get(
            pk=request.data.get('category'))
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
