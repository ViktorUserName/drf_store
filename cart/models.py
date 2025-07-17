import uuid

from django.db import models

from pizza.models import PizzaSize


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} on {self.date} at {self.time}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    pizza_size = models.ForeignKey(
        PizzaSize,
        on_delete=models.PROTECT,
        related_name='order_items'
    )
    quantity = models.PositiveIntegerField(default=1)

    @property
    def item_subtotal(self):
        return self.quantity * self.pizza_size.price

    def __str__(self):
        return (
            f"{self.quantity} x {self.pizza_size.pizza.name} "
            f"({self.pizza_size.get_size_display()}) for Order #{self.order.id}"
        )