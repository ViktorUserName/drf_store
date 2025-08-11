from rest_framework import viewsets
from .tasks import send_mail_task

from contact.models import ContactMessage
from contact.serializers import ContactSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        # 1. Сначала сохраняем объект в базе данных
        instance = serializer.save()
        print(f'Сообщение от {instance.name} успешно сохранено в БД.')

        # 2. Затем вызываем Celery-задачу для отправки письма
        send_mail_task.delay(instance.name, instance.email, instance.message)
        print(f"Задача Celery запущена для отправки письма от {instance.name}.")


