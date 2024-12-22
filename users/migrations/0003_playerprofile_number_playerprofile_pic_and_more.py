# Generated by Django 5.1.2 on 2024-12-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_coachprofile_team_playerprofile_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerprofile',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='prof/'),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='pos',
            field=models.CharField(choices=[('PG ', 'Point Guard '), ('SG', 'Shooting Guard'), ('SF', 'Small forward'), ('PF', 'Power forward'), ('C', 'Center')], max_length=50, null=True),
        ),
    ]