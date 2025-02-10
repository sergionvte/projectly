from django.db import models
from apps.accounts.models import User, Team

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='chat_files/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.content:
            return f"{self.sender.username}: {self.content[:30]}..."
        return f"{self.sender.username} sent a file"

