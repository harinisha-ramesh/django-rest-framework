# Generated by Django 5.1.2 on 2024-10-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewset', '0004_alter_product_is_deletable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_deletable',
            field=models.BooleanField(default=True),
        ),
    ]
