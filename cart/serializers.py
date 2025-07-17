from django.db import transaction
from rest_framework import serializers

from cart.models import OrderItem, Order
from pizza.models import PizzaSize


class PizzaSizeSerializer(serializers.ModelSerializer):
    pizza_id = serializers.IntegerField(source='pizza.id')
    pizza_name = serializers.CharField(source='pizza.name')

    class Meta:
        model = PizzaSize
        fields = ("pizza_id", 'pizza_name', "price", "size")



class OrderItemSerializer(serializers.ModelSerializer):
    pizza_id = serializers.IntegerField(source='pizza_size.pizza.id')
    pizza_name = serializers.CharField(source='pizza_size.pizza.name')
    pizza_price = serializers.DecimalField(source='pizza_size.price', decimal_places=2, max_digits=5)

    class Meta:
        model = OrderItem
        fields = ("pizza_id", 'pizza_name', "quantity", "pizza_price", "item_subtotal")


class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.UUIDField(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    total= serializers.SerializerMethodField()

    def get_total(self, obj):
        order_items = obj.items.all()
        return sum(item.item_subtotal for item in order_items)

    class Meta:
        model = Order
        fields = ("order_id",
                  "date",
                  "time",
                  "items",
                  "total",
                  )

# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True, write_only=False)
#     total = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Order
#         fields = ['order_id', 'date', 'time', 'items', 'total']
#         read_only_fields = ['order_id', 'date', 'time', 'total']
#
#     def get_total(self, obj):
#         return sum(item.get_total_item_price() for item in obj.items.all())
#
#     def create(self, validated_data):
#         items_data = validated_data.pop('items')
#         print(f"Received items_data: {items_data}")  # Добавьте эту строку
#
#         if not items_data:
#             raise serializers.ValidationError({"cart": "Cart cannot be empty."})
#
#         with transaction.atomic():
#             order = Order.objects.create(**validated_data)
#
#             merged_items = {}
#             for item_data in items_data:
#                 print(f"Processing item_data: {item_data}")  # Добавьте эту строку
#                 pizza_type_id = item_data.get('pizza', {}).get('id')
#                 size = item_data.get('size')
#                 print(f"Extracted: pizza_type_id={pizza_type_id}, size={size}")  # Добавьте эту строку
#
#                 if pizza_type_id is None or size is None:
#                     print("Error: pizza_type_id or size is None. Raising ValidationError.")  # Добавьте эту строку
#                     raise serializers.ValidationError(
#                         "Invalid item data: 'pizza.id' and 'size' are required for each cart item.")
#
#                 size_normalized = size.upper()  # Теперь вы уверены, что здесь .upper()
#                 print(f"Normalized size: {size_normalized}")  # Добавьте эту строку
#
#                 try:
#                     pizza_size_instance = PizzaSize.objects.get(
#                         pizza__id=pizza_type_id,
#                         size=size_normalized
#                     )
#                     print(f"Found PizzaSize: {pizza_size_instance}")  # Добавьте эту строку
#                 except PizzaSize.DoesNotExist:
#                     print(
#                         f"PizzaSize.DoesNotExist for pizza_type_id={pizza_type_id}, size={size_normalized}. Raising ValidationError.")  # Добавьте эту строку
#                     raise serializers.ValidationError(
#                         f"Pizza with type ID {pizza_type_id} and size '{size}' does not exist."
#                     )
#
#                 item_key = f"{pizza_type_id}_{size_normalized}"
#                 if item_key not in merged_items:
#                     merged_items[item_key] = {
#                         'pizza_size': pizza_size_instance,
#                         'quantity': 1
#                     }
#                 else:
#                     merged_items[item_key]['quantity'] += 1
#
#             order_items_to_create = []
#             for item_data in merged_items.values():
#                 order_items_to_create.append(
#                     OrderItem(
#                         order=order,
#                         pizza_size=item_data['pizza_size'],
#                         quantity=item_data['quantity']
#                     )
#                 )
#             OrderItem.objects.bulk_create(order_items_to_create)
#
#         return order