# Generated by Django 4.2.6 on 2023-10-07 00:31

from django.db import migrations, models
import games.models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='audio',
            field=models.FileField(upload_to=games.models.get_audio_upload_path),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to=games.models.get_image_upload_path),
        ),
    ]
