from django.db import models
from apps.accounts.models import User, Team

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tasks', null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'team'], name='unique_task_per_team')
        ]

    def __str__(self):
        return self.title

    def can_user_access(self, user):
        """Verifica si el usuario pertenece al equipo de la tarea."""
        return user in self.team.members.all()

class Evidence(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='evidences')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='task_evidences/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)