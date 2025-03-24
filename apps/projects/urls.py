from django.urls import path
from .views import create_project, project_detail, project_edit, check_project_similarity, generate_project_doc

urlpatterns = [
    path('project/create/', create_project, name='create_project'),
    path('project/<int:project_id>/', project_detail, name='project_detail'),
    path('project/<int:project_id>/edit/', project_edit, name='project_edit'),
    path('check-similarity/', check_project_similarity, name='check_project_similarity'),
    path('proyect/<int:project_id>/descargar/', generate_project_doc, name='download_project'),

]