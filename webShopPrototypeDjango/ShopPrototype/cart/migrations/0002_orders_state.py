# Generated by Django 4.2.3 on 2023-07-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='state',
            field=models.CharField(choices=[('NotProcessed', 'Not Processed'), ('InProgress', 'InProgress'), ('Processed', 'Processed')], default='NotProcessed', max_length=20, verbose_name='State'),
        ),
    ]
