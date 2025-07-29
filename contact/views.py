from rest_framework import viewsets

from contact.models import ContactMessage
from contact.serializers import ContactSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
