# Generated by Django 5.1.4 on 2025-03-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_alter_team_team_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_code',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
