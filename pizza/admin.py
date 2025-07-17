from django.contrib import admin
from pizza.models import Pizza


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)

