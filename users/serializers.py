from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField


class UserSerializer(ModelSerializer):
    full_name = SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
            "first_name",
            "last_name",
            "phone",
            "email",
            "address",
            "city",
            "state",
            "zip_code",
        ]

    def get_full_name(self, instance):
        full_name = None
        first_name = instance.first_name
        last_name = instance.last_name
        if first_name and last_name:
            full_name = f"{first_name} {last_name}"
        return full_name


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, data):
        user_response = super(CustomTokenObtainPairSerializer, self).validate(data)
        user_response.update({"user": UserSerializer(self.user).data})
        return user_response
