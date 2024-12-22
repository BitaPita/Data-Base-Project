# Generated by Django 5.1.2 on 2024-12-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='isplayed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matches',
            name='sc1',
            field=models.IntegerField(blank=0, null=True),
        ),
        migrations.AddField(
            model_name='matches',
            name='sc2',
            field=models.IntegerField(blank=0, null=True),
        ),
    ]