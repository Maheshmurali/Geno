# Generated by Django 5.0.3 on 2024-03-30 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_processor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image_file',
            new_name='Image_files',
        ),
    ]
