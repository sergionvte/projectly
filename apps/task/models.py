from django.db import models
from apps.accounts.models import User, Team

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True, default=None)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Evidence(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='evidence')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='task_evidences/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
