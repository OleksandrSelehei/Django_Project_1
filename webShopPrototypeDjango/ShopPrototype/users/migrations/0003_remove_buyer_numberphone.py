# Generated by Django 4.2.3 on 2023-07-09 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_buyer_numberphone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='numberphone',
        ),
    ]
