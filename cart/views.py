from rest_framework import viewsets, status, serializers
from rest_framework.response import Response

from cart.models import Order, OrderItem
from pizza.models import PizzaSize
from .serializers import PizzaSizeSerializer, OrderItemSerializer, OrderSerializer


# class OrderViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint, который позволяет просматривать и создавать заказы.
#     """
#     queryset = Order.objects.all().order_by('-date', '-time')
#     serializer_class = OrderSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         try:
#             self.perform_create(serializer)
#         except serializers.ValidationError as e:
#             return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"detail": "An unexpected error occurred during order creation.", "error": str(e)},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PizzaSizeViewSet(viewsets.ModelViewSet):
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
