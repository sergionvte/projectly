# Generated by Django 5.1.4 on 2025-03-01 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_delete_projectteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='embedding',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
