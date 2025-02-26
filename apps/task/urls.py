from django.urls import path
from .views import (
    task_list, task_detail, create_task,
    mark_task_complete, add_comment, upload_evidence
)

urlpatterns = [
    path('', task_list, name='task_list'),
    path('<int:task_id>/', task_detail, name='task_detail'),
    path('new-task/', create_task, name='create_task'),
    path('<int:task_id>/completar/', mark_task_complete, name='mark_task_complete'),
    path('<int:task_id>/comentario/', add_comment, name='add_comment'),
    path('<int:task_id>/subir-evidencia/', upload_evidence, name='upload_evidence'),
]