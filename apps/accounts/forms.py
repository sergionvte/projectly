from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Team

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'auth-form-control', 'placeholder': 'First Name', 'autofocus': True}),
            'last_name': forms.TextInput(attrs={'class': 'auth-form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'auth-form-control', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'auth-form-control', 'placeholder': 'Username'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'auth-form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'auth-form-control', 'placeholder': 'Confirm Password'})

        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email'].label = ''
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'auth-form-control', 'placeholder': 'Email', 'autofocus': True}),
        label='Email'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'auth-form-control', 'placeholder': 'Password'}),
        label='Contraseña'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_code']

    def save(self, user, commit=True):
        team = super().save(commit=False)
        team.created_by = user  # Asigna el usuario como creador
        if commit:
            team.save()
            team.members.add(user)  # Añadir al usuario como miembro
            user.team_assigned = team  # Asignar el equipo al usuario
            user.save()
        return team


class JoinTeamForm(forms.Form):
    team_code = forms.CharField(label="Código del equipo", max_length=10)

    def clean_team_code(self):
        team_code = self.cleaned_data.get('team_code')
        try:
            team = Team.objects.get(team_code=team_code)
        except Team.DoesNotExist:
            raise forms.ValidationError("El código ingresado no es válido.")
        return team