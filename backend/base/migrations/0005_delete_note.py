# Generated by Django 5.0.1 on 2024-02-09 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_meme_img_remove_meme_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]
