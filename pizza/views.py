import math
from datetime import datetime

from psycopg2 import DATETIME
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from pizza.models import Pizza, PizzaSize
from pizza.serializers import PizzaSerializer, PizzaSizeSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PizzaSizeViewSet(viewsets.ModelViewSet):
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer



class PizzaOfTheDayViewSet(APIView):

    def get(self, request, *args, **kwargs):
        pizzas = Pizza.objects.all()

        if not pizzas.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        days_since_epoch = math.floor(datetime.now().timestamp() / 86400)
        pizza_index = int(days_since_epoch % pizzas.count())
        pizza_of_the_day = pizzas[pizza_index]

        serializer = PizzaSerializer(pizza_of_the_day, context={'request': request})

        return Response(serializer.data)


