# Generated by Django 5.1.4 on 2025-03-23 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_alter_team_team_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_code',
            field=models.CharField(default='cnppkimkfm', max_length=10, unique=True),
        ),
    ]
