# Generated by Django 4.0.3 on 2022-04-13 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_player_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nba',
            name='players',
            field=models.ManyToManyField(null=True, to='main_app.player'),
        ),
    ]
