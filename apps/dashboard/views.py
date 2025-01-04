from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..projects.models import Project
from ..accounts.models import User

# Create your views here.
@login_required(login_url='/login')
def dashboard(request):
    project = Project.objects.filter(
        created_by__email=request.user.email
    ).first()
    return render(
        request,
        'dashboard/dashboard.html',
        {'project': project}
    )