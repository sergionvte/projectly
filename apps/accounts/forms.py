from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

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


class CreateTeamForm(forms.Form):
    project_assigned = forms.CharField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team_name'].label = ''
