# Generated by Django 5.0.1 on 2024-02-06 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_meme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='url',
            field=models.TextField(),
        ),
    ]
