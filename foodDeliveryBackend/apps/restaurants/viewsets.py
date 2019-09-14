from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
