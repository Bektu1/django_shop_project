# Generated by Django 4.2 on 2023-04-19 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default='image.jpg', upload_to='images'),
        ),
    ]