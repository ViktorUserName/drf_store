from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100, default="no name")
    category = models.CharField(max_length=100, default="no category")
    description = models.TextField(default="no description")
    image = models.CharField(max_length=255, default="", help_text="Пример: pizzas/hawaiian.webp")


    def __str__(self):
        return self.name


class PizzaSize(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="sizes")
    SIZES_CHOICES = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
    )
    size = models.CharField(choices=SIZES_CHOICES, max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    class Meta:
        unique_together = ('pizza', 'size')

    def __str__(self):
        return f"{self.pizza.name} ({self.get_size_display()}) - {self.price}"