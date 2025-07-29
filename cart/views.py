import time

from rest_framework import viewsets, status, serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from cart.models import Order, OrderItem
from .serializers import OrderItemSerializer, OrderSerializer, OrderCreateSerializer, PastOrdersReadSerializer, \
    PastOrderDetailSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return OrderCreateSerializer
        return super().get_serializer_class()


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class PastOrdersPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PastOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = PastOrdersReadSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'update':
            return PastOrderDetailSerializer
        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        self.pagination_class = None
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.pagination_class = PastOrdersPagination
        return super().list(request, *args, **kwargs)
    #
    # def get_queryset(self):
    #     # Задержка будет применяться при каждом получении queryset
    #     time.sleep(1)
    #     return super().get_queryset()
