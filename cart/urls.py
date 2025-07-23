from django.urls import path
from rest_framework.routers import DefaultRouter

from cart.views import OrderItemViewSet, OrderViewSet, PizzaSizeViewSet

router = DefaultRouter()

router.register(r'pizzasize/', PizzaSizeViewSet)
router.register(r'itemorder', OrderItemViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls