# Generated by Django 3.2.12 on 2022-03-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0006_dictateur_dictateur_blason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictateur',
            name='dictateur_election',
        ),
        migrations.AddField(
            model_name='dictateur',
            name='dictateur_election',
            field=models.ManyToManyField(blank=True, null=True, to='election.Election'),
        ),
    ]
