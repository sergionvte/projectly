from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse
from apps.accounts.models import Team
from .models import Message
import os

@login_required
def chat_view(request, team_id):
    try:
        team = Team.objects.get(id=team_id)
        if request.user not in team.members.all() and request.user.username != team.project.tutor:
            return render(request, "403.html")
        messages = Message.objects.filter(team=team).order_by("timestamp")
        return render(request, "chat/chat.html", {"team": team, "messages": messages})
    except Team.DoesNotExist:
        return render(request, "404.html")

@login_required
def upload_file(request, team_id):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        file_path = default_storage.save(os.path.join("chat_files", file.name), ContentFile(file.read()))
        file_url = default_storage.url(file_path)

        team = Team.objects.get(id=team_id)
        message = Message.objects.create(
            sender=request.user,
            team=team,
            content=file_url
        )
        return JsonResponse({"file_url": file_url, "timestamp": message.timestamp.strftime("%H:%M")})
    return JsonResponse({"error": "No file uploaded"}, status=400)

