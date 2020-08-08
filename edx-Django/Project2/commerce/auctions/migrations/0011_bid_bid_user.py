# Generated by Django 3.0.8 on 2020-08-08 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_listings_item_starting_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]