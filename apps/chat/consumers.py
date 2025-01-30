import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import AnonymousUser
from .models import Message
from apps.accounts.models import User, Team

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.team_id = self.scope["url_route"]["kwargs"]["team_id"]
        self.user = self.scope.get("user", AnonymousUser())

        if self.user.is_authenticated and await self.user_belongs_to_team():
            self.room_group_name = f"chat_{self.team_id}"
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def user_belongs_to_team(self):
        """Verifica si el usuario pertenece al equipo o es tutor."""
        try:
            team = await sync_to_async(Team.objects.get)(id=self.team_id)
            return self.user in await sync_to_async(lambda: list(team.members.all()))() or self.user.username == team.project.tutor
        except Team.DoesNotExist:
            return False

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data["content"]

        if self.user.is_authenticated:
            sender = self.user
            team = await sync_to_async(Team.objects.get)(id=self.team_id)

            message = await sync_to_async(Message.objects.create)(
                sender=sender, team=team, content=content
            )

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "sender": sender.username,
                    "content": content,
                    "timestamp": str(message.timestamp),
                }
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "sender": event["sender"],
            "content": event["content"],
            "timestamp": event["timestamp"],
        }))
