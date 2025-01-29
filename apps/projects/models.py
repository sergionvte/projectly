from django.db import models
from datetime import datetime
from ..accounts.models import User

# Create your models here.
class Project(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=50)
    goal = models.TextField(null=True)
    description = models.TextField()
    tutor = models.CharField(max_length=50)
    project_phase = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    team_assigned = models.OneToOneField('accounts.Team', on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    project_url = models.CharField(max_length=100, null=True, blank=True)
    project_tiktok = models.CharField(max_length=100, null=True, blank=True)
    project_instagram = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    # the folloing line needs 'enctype="multipart/form-data"' in the form
    attachment = models.FileField(upload_to='attachments/')
    created_at = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)