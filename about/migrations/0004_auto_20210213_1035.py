# Generated by Django 3.1.5 on 2021-02-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='legal_document'),
        ),
    ]