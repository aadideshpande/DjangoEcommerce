# Generated by Django 3.0.3 on 2020-07-07 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200707_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Order',
            new_name='order',
        ),
    ]
