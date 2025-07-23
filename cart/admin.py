from django.contrib import admin

from cart.models import Order, OrderItem, OrderPizzaItem, OrderPizza

admin.site.register(Order)

admin.site.register(OrderItem)

admin.site.register(OrderPizzaItem)

admin.site.register(OrderPizza)