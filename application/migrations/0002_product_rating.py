# Generated by Django 5.1.2 on 2024-10-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]