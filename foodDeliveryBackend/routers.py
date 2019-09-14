from rest_framework import routers
from .apps.foods.viewsets import FoodViewSet

router = routers.DefaultRouter()

router.register('foods', FoodViewSet)
