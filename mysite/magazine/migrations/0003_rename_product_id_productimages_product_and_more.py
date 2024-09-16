# Generated by Django 5.0.7 on 2024-09-11 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_productimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimages',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='products',
            name='main_image_product',
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image_path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
