from rest_framework.routers import DefaultRouter

from contact.views import ContactMessageViewSet

router = DefaultRouter()

router.register(r'', ContactMessageViewSet)

urlpatterns = router.urls