# Generated by Django 4.0.3 on 2022-04-13 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_nba_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('pg', 'point guard'), ('sg', 'shooting guard'), ('sf', 'small forward'), ('pf', 'power forward'), ('c', 'center')], max_length=50)),
            ],
        ),
    ]
