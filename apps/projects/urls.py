from django.urls import path
from .views import create_project, project_detail, project_edit

urlpatterns = [
    path('project/create/', create_project, name='create_project'),
    path('project/<int:project_id>/', project_detail, name='project_detail'),
    path('project/<int:project_id>/edit/', project_edit, name='project_edit'),
]