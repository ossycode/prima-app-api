"""
Views for the user API.
"""
from core.models import User
from users.serializers import UserSerializer
from rest_framework import generics


class CreateUserView(generics.ListCreateAPIView):
    """Create a new user in the system."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    """Get a single user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
  