"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, username, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email or not username:
            raise ValueError("User must have an email address and a username. ")
        user = self.model( email=self.normalize_email(email),username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, username, password):
        """Create and return a new superuser."""
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_staff= models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
   
