from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from .forms import RegistrationForm, JoinTeamForm

# Create your views here.
class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


from django.contrib.auth.views import LoginView
from .forms import LoginForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


from django.contrib.auth import logout as logout_function

def logout(request):
    logout_function(request)
    return redirect('landing')


from .models import Team
from .forms import TeamForm
from django.contrib.auth.decorators import login_required

@login_required
def create_team(request):
    if request.user.team_assigned:
        messages.error(request, "Ya perteneces a un equipo.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(request.user)
            messages.success(request, f"Equipo {team.team_code} creado exitosamente.")
            return redirect('dashboard')
    else:
        form = TeamForm()

    return render(request, 'accounts/create_team.html', {'form': form})


@login_required
def join_team(request):
    if request.user.team_assigned:
        messages.error(request, "Ya perteneces a un equipo. No puedes unirte a otro.")
        return redirect('dashboard')

    if request.method == 'POST':
        team_code = request.POST.get('team_code')
        team = get_object_or_404(Team, team_code=team_code)

        request.user.team_assigned = team
        request.user.save(update_fields=['team_assigned'])

        team.members.add(request.user)
        messages.success(request, f"Te uniste exitosamente al equipo {team.team_code}.")
        return redirect('dashboard')

    return render(request, 'accounts/join_team.html')



from django.shortcuts import render, get_object_or_404
from .models import Team, User

@login_required
def team_detail(request, id):
    if not request.user.team_assigned:
        return redirect('dashboard')

    team = get_object_or_404(Team, id=id)  # Busca por ID en lugar de team_code
    return render(request, 'accounts/team_detail.html', {'team': team})


def remove_member(request, team_id, member_id):
    team = get_object_or_404(Team, id=team_id)
    member = get_object_or_404(User, id=member_id)

    if team.created_by == request.user:
        if member in team.members.all():
            team.members.remove(member)
            member.team_assigned = None
            member.save(update_fields=['team_assigned'])
            messages.success(request, f"El miembro {member.first_name} {member.last_name} ha sido eliminado exitosamente.")

        else:
            messages.error(request, "Este miembro no pertenece a este equipo.")
    else:
        messages.error(request, "Solo el líder del equipo puede eliminar miembros.")

    return redirect('team_detail', team_id)
