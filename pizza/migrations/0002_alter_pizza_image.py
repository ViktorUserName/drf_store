# Generated by Django 5.2.4 on 2025-07-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(upload_to='pizzas/'),
        ),
    ]
