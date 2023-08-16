# Generated by Django 3.2 on 2023-05-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_subscription_films'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='payment_gw_price_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='Latest Price ID for this subscription plan on payment gateway'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='description',
            field=models.TextField(default='desc', verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='payment_gw_product_id',
            field=models.CharField(blank=True, default='?null?', max_length=255, verbose_name='Actual Product ID on payment gateway'),
            preserve_default=False,
        ),
    ]
