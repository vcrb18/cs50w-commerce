# Generated by Django 4.1 on 2022-08-15 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_comments_bids_auction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='bids',
        ),
        migrations.AlterField(
            model_name='auction',
            name='price',
            field=models.IntegerField(),
        ),
    ]
