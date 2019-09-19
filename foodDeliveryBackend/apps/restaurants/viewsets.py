from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().prefetch_related(
        'categories', 'categories__foods')
    serializer_class = RestaurantSerializer

    def list(self, request):

        if request.query_params == {}:
            queryset = Restaurant.objects.all()
        else:
            query = request.query_params['search']
            queryset = Restaurant.objects.filter(name__icontains=query)

        serializer = RestaurantSerializer(
            queryset, many=True, fields=('id', 'name', 'address',))
        return Response(serializer.data)

    def create(self, request):
        if not request.user.is_restaurant:
            return Response({'message': 'unauthorized'}, 401)

        serializer = RestaurantSerializer(
            data=request.data, fields=('id', 'name', 'address',))

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save(user=request.user)

        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
