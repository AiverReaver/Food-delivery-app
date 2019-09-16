from rest_framework import routers
from apps.foods.viewsets import FoodViewSet, FoodCategoryViewSet
from apps.restaurants.viewsets import RestaurantViewSet

router = routers.DefaultRouter()

router.register('foods', FoodViewSet)
router.register('foodcategories', FoodCategoryViewSet)
router.register('restaurants', RestaurantViewSet)
