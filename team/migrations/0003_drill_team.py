# Generated by Django 5.1.2 on 2024-11-13 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_drill_teams_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='drill',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='team.teams'),
        ),
    ]
