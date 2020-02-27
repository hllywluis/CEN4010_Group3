# Generated by Django 3.0.3 on 2020-02-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Browse', '0008_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='top_seller',
            field=models.BooleanField(null=True),
        ),
    ]
