from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Team

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'career', 'password1', 'password2']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'auth-form-control', 'placeholder': 'Nombre', 'autofocus': True}),
            'Apellido': forms.TextInput(attrs={'class': 'auth-form-control', 'placeholder': 'Apellido'}),
            'Email': forms.EmailInput(attrs={'class': 'auth-form-control', 'placeholder': 'Email'}),
            'Nombre de usuario': forms.TextInput(attrs={'class': 'auth-form-control', 'placeholder': 'Nombre de usuario'}),
            'Carrera': forms.TextInput(attrs={'class': 'auth-form-control', 'placeholder': 'Carrera'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre', 'autofocus': True})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Apellido'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email', 'autofocus': False})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre de usuario'})
        self.fields['career'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Carrera'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmar contraseña'})

        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email'].label = ''
        self.fields['username'].label = ''
        self.fields['career'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autofocus': True}),
        label='Email'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label='Contraseña'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = []

    def save(self, user, commit=True):
        team = super().save(commit=False)
        team.created_by = user
        if commit:
            team.save()
            team.members.add(user)
            user.team_assigned = team
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