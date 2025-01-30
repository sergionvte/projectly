from django.urls import path
from .views import chat_view

urlpatterns = [
    path("chat/<int:team_id>", chat_view, name="team_chat"),
]
