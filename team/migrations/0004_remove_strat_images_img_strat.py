# Generated by Django 5.1.2 on 2024-11-19 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_img_pos_strat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strat',
            name='images',
        ),
        migrations.AddField(
            model_name='img',
            name='strat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='team.strat'),
        ),
    ]