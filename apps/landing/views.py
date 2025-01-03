from django.shortcuts import render, redirect

# Create your views here.
def landing(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing/landing.html')