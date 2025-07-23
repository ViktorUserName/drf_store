from rest_framework import viewsets, status, serializers
from rest_framework.response import Response

from cart.models import Order, OrderItem
from pizza.models import PizzaSize
from .serializers import OrderItemSerializer, OrderSerializer, OrderCreateSerializer, PizzaSizeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return OrderCreateSerializer
        return super().get_serializer_class()


class PizzaSizeViewSet(viewsets.ModelViewSet):
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
