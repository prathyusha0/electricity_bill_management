# Generated by Django 3.0.7 on 2020-06-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200616_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='meter',
            name='brand_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='modelnumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]