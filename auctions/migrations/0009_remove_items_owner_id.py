# Generated by Django 4.2.3 on 2023-07-31 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_items_owner_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='owner_id',
        ),
    ]