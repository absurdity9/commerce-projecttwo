# Generated by Django 4.2.3 on 2023-07-28 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_comments_listing_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='listing_id',
        ),
        migrations.AddField(
            model_name='comments',
            name='item_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
    ]