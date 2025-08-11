from celery import shared_task
from contact.models import ContactMessage
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_mail_task(*args, **kwargs):
    try:
        name = args[0]
        email = args[1]
        message = args[2]

        print(f'Executing task {name} {email} {message}')

        subject = f'Новое сообщение от контактной форты от {name}'
        email_message = f'Имя {name}\nEmail {email}\nMessage:\n{message}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.ADMIN_EMAIL]

        send_mail(subject, email_message, from_email, recipient_list, fail_silently=False)
        print(f'Письмо от {name} успешно отправлено на {settings.ADMIN_EMAIL}')

        # ContactMessage.objects.create(
        #     name=name,
        #     email=email,
        #     message=message,
        # )
        print(f'Message was saved {name}')
    except Exception as e:
        print(f'Error in task: {e}')
