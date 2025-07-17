from rest_framework import serializers

from pizza.models import Pizza, PizzaSize
from settings import settings


class PizzaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    sizes = serializers.SerializerMethodField()

    class Meta:
        model = Pizza
        fields = ('id', 'name', 'sizes','image', 'image_url', 'category', 'description')

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


# class PizzaOfTheDay(PizzaSerializer):