# Generated by Django 5.1.1 on 2024-09-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counseling', '0002_counselingmaterial_image_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counselingmaterial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='materials/images/'),
        ),
    ]
