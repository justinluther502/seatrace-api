# Generated by Django 3.2.7 on 2021-10-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0008_auto_20211019_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rower',
            name='mmr',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rower',
            name='mmr_uncertainty',
            field=models.FloatField(),
        ),
    ]
