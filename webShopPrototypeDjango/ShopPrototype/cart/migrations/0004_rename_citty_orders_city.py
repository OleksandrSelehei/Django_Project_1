# Generated by Django 4.2.3 on 2023-07-13 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_orders_photo_remove_orders_product_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='citty',
            new_name='city',
        ),
    ]
