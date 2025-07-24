from django.db import transaction
from rest_framework import serializers
from cart.models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    pizza_id = serializers.IntegerField(source='pizza_size.pizza.id')
    pizza_name = serializers.CharField(source='pizza_size.pizza.name')
    pizza_price = serializers.DecimalField(source='pizza_size.price', decimal_places=2, max_digits=5)
    pizza_size = serializers.CharField(source='pizza_size.size')

    class Meta:
        model = OrderItem
        fields = ("pizza_id", 'pizza_name','pizza_size', "quantity", "pizza_price", "item_subtotal")


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


class PastOrdersReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    class OrderItemCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = ('order_id','pizza_size', 'quantity')

    order_id = serializers.UUIDField(read_only=True)
    items = OrderItemCreateSerializer(many=True, required=False)

    def create(self, validated_data):
        orderitem_data = validated_data.pop('items')

        with transaction.atomic():
            order = Order.objects.create(**validated_data)

            for item in orderitem_data:
                OrderItem.objects.create(order=order, **item)

        return order

    def update(self, instance, validated_data):
        orderitem_data = validated_data.pop('items')

        with transaction.atomic():
            instance = super().update(instance, validated_data)

            if orderitem_data is not None:
                # Clear existing items (optional, depends on requirements)
                instance.items.all().delete()

                # Recreate items with the updated data
                for item in orderitem_data:
                    OrderItem.objects.create(order=instance, **item)
        return instance

    class Meta:
        model = Order
        fields = (
            'order_id',
            'date',
            'time',
            'items',
        )

