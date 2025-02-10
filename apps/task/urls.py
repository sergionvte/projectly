from django.urls import path
from .views import (
    task_list, task_detail, create_task,
    mark_task_complete, add_comment, upload_evidence
)

urlpatterns = [
    path('', task_list, name='task_list'),
    path('<int:pk>/', task_detail, name='task_detail'),
    path('new-task/', create_task, name='create_task'),
    path('<int:pk>/completar/', mark_task_complete, name='mark_task_complete'),
    path('<int:pk>/comentario/', add_comment, name='add_comment'),
    path('<int:pk>/subir-evidencia/', upload_evidence, name='upload_evidence'),
]