import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
celery = Celery('settings')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.conf.update(
    accept_content=['json'],
    task_serializer='json',
    result_serializer='json',
)
celery.autodiscover_tasks()
# celery.conf.update(
#     imports=['contact.task']
# )