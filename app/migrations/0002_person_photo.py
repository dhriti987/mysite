# Generated by Django 3.2.10 on 2022-02-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(default='hetvi.jpg', upload_to='person'),
        ),
    ]
