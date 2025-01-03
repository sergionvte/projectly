from django.db import models

# Create your models here.
class Project(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    tutor = models.CharField(max_length=50)
    project_phase = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=50)
    team_assigned = models.IntegerField(null=False)
    github_url = models.CharField(max_length=100)
    project_url = models.CharField(max_length=100)


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


class ProjectTeam(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    role = models.CharField(max_length=50)