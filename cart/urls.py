from django.urls import path
from rest_framework.routers import DefaultRouter

from cart.views import OrderItemViewSet, OrderViewSet, PastOrderViewSet

router = DefaultRouter()


router.register(r'itemorder', OrderItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'past-orders', PastOrderViewSet, basename='past-orders')


urlpatterns = router.urls