# Generated by Django 3.2.12 on 2022-03-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0004_auto_20220319_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictateur',
            name='dictateur_avatar',
            field=models.ImageField(blank=True, upload_to='avatar'),
        ),
    ]