# Generated by Django 5.1.4 on 2025-02-05 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_team_team_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_tutor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_code',
            field=models.CharField(default='95vxb65jz7', max_length=10, unique=True),
        ),
    ]
