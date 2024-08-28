# Generated by Django 5.0.7 on 2024-08-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_categorypost_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
