# Generated by Django 5.1.4 on 2025-01-03 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_team_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='career',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
