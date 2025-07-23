from rest_framework import serializers

from pizza.models import Pizza, PizzaSize
from settings import settings


class PizzaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    sizes = serializers.SerializerMethodField()
    # pizza_id = serializers.SerializerMethodField()

    class Meta:
        model = Pizza
        fields = ('id', 'name', 'sizes','image', 'image_url', 'category', 'description')

    # def get_pizza_id(self, instance):
    #     return instance.sizes.id

    def get_sizes(self, obj):
        return {
            size.size : size.price for size in obj.sizes.all()
        }

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            relative_url = f"{settings.MEDIA_URL}{obj.image}"
            return request.build_absolute_uri(relative_url) if request else relative_url
        return None


class PizzaSizeSerializer(serializers.ModelSerializer):
    # pizza_id = serializers.IntegerField(source='pizza.id')
    name = serializers.CharField(source='pizza.name')
    # image_url = serializers.CharField(source='pizza.image_url')
    category = serializers.CharField(source='pizza.category')
    description = serializers.CharField(source='pizza.description')
    image_url = serializers.SerializerMethodField()
    # price = serializers.SerializerMethodField()

    # fields = ('id', 'name', 'sizes', 'image', 'image_url', 'category', 'description')

    class Meta:
        model = PizzaSize
        fields = ("id", 'name',"size", 'image_url','category', 'description')

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.pizza.image:
            relative_url = f"{settings.MEDIA_URL}{obj.pizza.image}"
            return request.build_absolute_uri(relative_url) if request else relative_url
        return None