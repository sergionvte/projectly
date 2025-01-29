# Generated by Django 5.1.4 on 2025-01-29 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_team_team_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_code',
            field=models.CharField(default='szduuvurav', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='team_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.team'),
        ),
    ]
