from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ProjectCreationForm

class ProjectCreationView(CreateView):
    template_name = 'projects/create_project.html'
    form_class = ProjectCreationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
