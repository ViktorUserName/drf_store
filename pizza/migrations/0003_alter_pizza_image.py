# Generated by Django 5.2.4 on 2025-07-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_alter_pizza_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.CharField(default='', help_text='Пример: pizzas/hawaiian.webp', max_length=255),
        ),
    ]
