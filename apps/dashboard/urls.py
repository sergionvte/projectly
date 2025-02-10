from django.urls import path
from .views import dashboard, tutor_dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('tutor/dashboard/<int:project_id>/', tutor_dashboard, name='tutor_dashboard'),
]