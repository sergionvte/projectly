import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.files.base import ContentFile
import base64
from .models import Message
from apps.accounts.models import User, Team

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.team_id = self.scope["url_route"]["kwargs"]["team_id"]
        self.user = self.scope.get("user")

        if self.user.is_authenticated and await self.user_belongs_to_team():
            self.room_group_name = f"chat_{self.team_id}"
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def user_belongs_to_team(self):
        try:
            team = await sync_to_async(Team.objects.get)(id=self.team_id)
            return self.user in await sync_to_async(lambda: list(team.members.all()))() or self.user.username == team.project.tutor
        except Team.DoesNotExist:
            return False

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data.get("content", "")
        file_data = data.get("file", None)

        if self.user.is_authenticated:
            sender = self.user
            team = await sync_to_async(Team.objects.get)(id=self.team_id)

            message_data = {"sender": sender, "team": team}

            if content:
                message_data["content"] = content

            if file_data:
                format, file_str = file_data.split(';base64,')
                ext = format.split('/')[-1]
                file_name = f"chat_{sender.id}_{team.id}.{ext}"
                message_data["file"] = ContentFile(base64.b64decode(file_str), name=file_name)

            message = await sync_to_async(Message.objects.create)(**message_data)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "sender": sender.username,
                    "content": content,
                    "file": message.file.url if message.file else None,
                    "timestamp": str(message.timestamp),
                }
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "sender": event["sender"],
            "content": event["content"],
            "file": event["file"],
            "timestamp": event["timestamp"],
        }))