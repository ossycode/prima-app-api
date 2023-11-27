"""
Serializers for the user API View.
"""

from rest_framework import serializers
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = User
        fields = ['id','email','username', 'password', 'name']
        read_only_fields= ['id']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return User.objects.create_user(**validated_data)
   