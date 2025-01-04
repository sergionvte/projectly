from django.urls import path
from .views import ProjectCreationView

urlpatterns = [
    path('create/', ProjectCreationView.as_view(), name='create_project'),
]