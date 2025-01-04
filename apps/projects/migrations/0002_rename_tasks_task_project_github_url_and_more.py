# Generated by Django 5.1.4 on 2025-01-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
