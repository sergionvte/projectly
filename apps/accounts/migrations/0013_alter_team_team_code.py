# Generated by Django 5.1.4 on 2025-01-29 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_team_team_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_code',
            field=models.CharField(default='8ht8ukjnge', max_length=10, unique=True),
        ),
    ]
