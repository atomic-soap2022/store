# Generated by Django 4.1.3 on 2023-02-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_checked',
            field=models.BooleanField(default=False, verbose_name='Проверено'),
        ),
    ]
