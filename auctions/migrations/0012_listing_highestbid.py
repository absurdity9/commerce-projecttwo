# Generated by Django 4.2.3 on 2023-08-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='highestbid',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]
