# Generated by Django 3.2.10 on 2022-02-16 09:53

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_person_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(default='hetvi.jpg', upload_to=app.models.create_path),
        ),
    ]
