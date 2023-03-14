from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from .models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None
        try:
            auth_token = auth_header.split(" ")[1]
            payload = jwt.decode(auth_token, settings.SECRET_KEY)
            email = payload["email"]
            user = User.objects.get(email=email)
            return (user, None)
        except (jwt.DecodeError, User.DoesNotExist):
            raise exceptions.AuthenticationFailed("Invalid token")
