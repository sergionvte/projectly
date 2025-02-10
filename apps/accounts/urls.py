from django.urls import path
from .views import (
    RegisterView, CustomLoginView, logout, create_team, join_team, team_detail, remove_member
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),

    # Teams
    path('team/create/', create_team, name='create_team'),
    path('team/join/', join_team, name='join_team'),
        path('team/<int:team_id>/remove_member/<int:member_id>/', remove_member, name='remove_member'),
    path('team/<int:id>/', team_detail, name='team_detail'),
]