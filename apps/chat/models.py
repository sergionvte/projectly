from django.db import models
from apps.accounts.models import User, Team

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:30]}..."
