# Generated by Django 2.2.2 on 2021-02-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products_Details', '0012_auto_20210212_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image1',
            field=models.ImageField(default='default.jpg', upload_to='product_image'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='image2',
            field=models.ImageField(default='default.jpg', upload_to='product_image'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='image3',
            field=models.ImageField(default='default.jpg', upload_to='product_image'),
        ),
    ]
