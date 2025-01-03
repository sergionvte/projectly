from django.urls import path
from .views import RegisterView, CustomLoginView, logout

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]