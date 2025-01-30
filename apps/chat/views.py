from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.accounts.models import Team
from .models import Message

@login_required
def chat_view(request, team_id):
    try:
        team = Team.objects.get(id=team_id)
        if request.user not in team.members.all() and request.user.username != team.project.tutor:
            return render(request, "403.html")  # Página de acceso denegado
        messages = Message.objects.filter(team=team).order_by("timestamp")
        return render(request, "chat/chat.html", {"team": team, "messages": messages})
    except Team.DoesNotExist:
        return render(request, "404.html")  # Página de equipo no encontrado
