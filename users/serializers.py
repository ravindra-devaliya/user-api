from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, data):
        return super(CustomTokenObtainPairSerializer, self).validate(data)
