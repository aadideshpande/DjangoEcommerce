# Generated by Django 3.0.3 on 2020-07-07 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, default='placeholder.jpg', null=True, upload_to=''),
        ),
    ]