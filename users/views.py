"""
Views for the user API.
"""
from core.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class CreateUserView(generics.ListCreateAPIView):
    """Create a new user in the system or retrieve all users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        Create a new user.

        Expected request format:
        - Method: POST
        - Endpoint: /api/users/
        - Data: JSON payload with fields: email, username,name, password

        Response format:
        - HTTP status code: 201 Created
        - Data returned: User information for the created user
        """
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Retrieve all users.

        Expected request format:
        - Method: GET
        - Endpoint: /api/users/

        Response format:
        - HTTP status code: 200 OK
        - Data returned: List of user information
        """
        return self.list(request, *args, **kwargs)
    

class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
     """
    API Endpoint for managing a single user.
    ...
    """
     queryset = User.objects.all()
     serializer_class = UserSerializer

     def get(self, request, *args, **kwargs):
        """
        Retrieve a single user by ID.

         Response format:
         - If user exists: Return user information (status code: 200 OK)
         - If user does not exist: Return 404 error

        Error Handling:
        - 404: Not found
        """
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
     

     def patch(self, request, *args, **kwargs):
        """
        Update a user by ID.

        Response format:
        - If update successful: Return updated user information (status code: 200 OK)
        - If user does not exist: Return 404 error
        - If input data is invalid: Return 400 error

        Error Handling:
        - 404: Not found
        - 400: Invalid input data
        """
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, *args, **kwargs):
        """
        Delete a user by ID.

        Response format:
        - If delete successful: No content (status code: 204 No Content)

        Error Handling:
        - 404: Not found
        """
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)