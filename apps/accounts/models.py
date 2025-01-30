from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string


class UserManager(BaseUserManager):
    """
    Personalized user model manager.
    """
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Email field is required.'))
        if not username:
            raise ValueError(_('Username field is required.'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)  # Encrypt the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError(_('Superuser needs to have is_staff=True.'))
        if not extra_fields.get('is_superuser'):
            raise ValueError(_('Superuser needs to have is_superuser=True.'))

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Personalized user model.
    """
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Password is managed by AbstractBaseUser
    team_assigned = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    career = models.CharField(max_length=255, blank=True)
    role = models.CharField(
        max_length=50,
        choices=[
            ('admin', 'Admin'),
            ('user', 'User'),
            ('moderator', 'Moderator'),
        ],
        default='user'
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)  # Active or inactive user
    is_staff = models.BooleanField(default=False)  # Staff user

    # Configure the manager
    objects = UserManager()

    # Define which field will be used as the unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Required fields when creating a user

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def get_short_name(self):
        return self.first_name or self.email


class Team(models.Model):
    id = models.AutoField(primary_key=True)  # Se genera automáticamente, pero lo hacemos explícito
    project_assigned = models.ForeignKey('projects.Project', on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    team_code = models.CharField(max_length=10, unique=True, default=get_random_string(10).lower())
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams', null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.created_by and self.created_by not in self.members.all():
            self.members.add(self.created_by)  # Agrega automáticamente al creador

    def __str__(self):
        return f"Team {self.id}"
