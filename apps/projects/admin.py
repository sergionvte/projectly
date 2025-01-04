from django.contrib import admin
from .models import Project, Task, ProjectTeam, Comment

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(ProjectTeam)
admin.site.register(Comment)
