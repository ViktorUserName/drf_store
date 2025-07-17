from django.urls import path
from rest_framework.routers import DefaultRouter

# from cart.views import OrderViewSet
from pizza.views import PizzaViewSet, PizzaOfTheDayViewSet

router = DefaultRouter()
router.register(r'pizzas', PizzaViewSet, basename='pizza')
# router.register(r'orders', OrderViewSet, basename='order')

custom_urlpatterns = [
    path(r'pizza-of-the-day/', PizzaOfTheDayViewSet.as_view(), name='pizza-of-the-day')
]

urlpatterns = router.urls + custom_urlpatterns