# Generated by Django 4.1.3 on 2022-11-19 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_catagory_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/static'),
        ),
    ]
