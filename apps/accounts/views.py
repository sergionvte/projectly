from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegistrationForm

# Create your views here.
class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


from django.contrib.auth.views import LoginView
from .forms import LoginForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


from django.contrib.auth import logout as logout_function

def logout(request):
    logout_function(request)
    return redirect('landing')