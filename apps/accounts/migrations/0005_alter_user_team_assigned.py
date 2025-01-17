# Generated by Django 5.1.4 on 2025-01-05 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='team_assigned',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.team'),
        ),
    ]
