# Generated by Django 3.2.12 on 2022-03-18 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='election',
            name='election_dictateur',
        ),
        migrations.RemoveField(
            model_name='election',
            name='election_paysan',
        ),
        migrations.AddField(
            model_name='dictateur',
            name='dictateur_election',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='election.election'),
        ),
        migrations.AddField(
            model_name='paysan',
            name='paysan_election',
            field=models.ManyToManyField(to='election.Election'),
        ),
    ]
