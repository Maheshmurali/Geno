# Generated by Django 5.0.3 on 2024-03-30 18:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_processor', '0003_image_delete_image_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
