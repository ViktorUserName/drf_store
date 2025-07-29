from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время отправки")

    class Meta:
        verbose_name = "Контактное сообщение"
        verbose_name_plural = "Contact masseges"
        ordering = ['-created_at']

    def __str__(self):
        return f"Сообщение от {self.name} ({self.email}) - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
