"""
Views for the user API
"""

from rest_framework import generics, authentication, permissions
from user.serializers import UsdrSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings



class CreateUserView(generics.CreateAPIView):
    serializer_class = UsdrSerializer

class CreateTokenView(ObtainAuthToken):
    """CReate a new auth tinen for user. """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):

    serializer_class = UsdrSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

