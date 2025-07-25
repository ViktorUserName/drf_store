# Generated by Django 5.2.4 on 2025-07-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no name', max_length=100)),
                ('category', models.CharField(default='no category', max_length=100)),
                ('description', models.TextField(default='no description')),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='medium', max_length=20)),
                ('image', models.ImageField(upload_to='pizza/')),
            ],
        ),
    ]
