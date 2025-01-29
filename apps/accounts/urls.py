from django.urls import path
from .views import RegisterView, CustomLoginView, logout, create_team, join_team, team_detail

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),

    # Teams
    path('team/create/', create_team, name='create_team'),
    path('team/join/', join_team, name='join_team'),
    path('team/details/', team_detail, name='team_detail'),
]